from flask import Flask, request, jsonify, render_template
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import re

app = Flask(__name__, template_folder="templates")

# Load model
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    truncation=True,
    do_sample=True,
    temperature=0.7,
)

llm = HuggingFacePipeline(pipeline=pipe)

# Vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 10})

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Bulletify any text (clean line breaks, remove embedded bullets, etc.)
def bulletify(text):
    # Remove repeated bullets and split clearly
    text = text.replace("•", "").replace(" -", ":")
    lines = re.split(r'(?<=[.!?])\s+', text.strip())
    bullets = [f"• {line.strip()}" for line in lines if len(line.strip()) > 3]
    return "\n".join(bullets)

# Extract and format top 3 documents cleanly
def extract_clean_snippets(docs, limit=3):
    clean_snippets = []
    for doc in docs[:limit]:
        content = doc.page_content.strip().replace("\n", " ")
        lines = re.split(r'(?<=[.!?])\s+', content)
        for line in lines:
            line = line.strip()
            if len(line) > 20:
                line = line.replace("•", "").strip()
                clean_snippets.append(f"• {line}")
    return "\n".join(clean_snippets)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("message")
    if not query:
        return jsonify({"error": "No message provided"}), 400

    # Generate answer
    result = qa_chain.invoke({"query": query})
    answer = bulletify(result["result"])

    # Add context
    docs = retriever.get_relevant_documents(query)
    context = extract_clean_snippets(docs)

    return jsonify({
        "answer": f"{answer}\n\n📄 Context Snippets:\n{context}"
    })

if __name__ == "__main__":
    app.run(port=5000)
