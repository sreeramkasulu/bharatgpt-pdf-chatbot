from flask import Flask, request, jsonify, render_template
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import re

app = Flask(__name__, template_folder="templates")

# Load compact model
model_name = "MBZUAI/LaMini-Flan-T5-248M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=256,
    max_new_tokens=100,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

# Load FAISS store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 5})

# Prompt Template
custom_prompt = PromptTemplate.from_template("""
You are BharatGPT, an expert in India’s biomaterials industry, sustainability policies, and circular economy regulations.

Answer the question using only the context below. Do not guess or add information beyond the context.

If the answer cannot be found in the context, respond with:
"Based on the available documents, no specific answer is found for this query."

Respond in 2–4 factual bullet points.

Context:
{context}

Question:
{question}

Answer:
""")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": custom_prompt}
)

# Text truncation
def truncate_text(text, max_tokens=350):
    words = text.split()
    return " ".join(words[:max_tokens]) if len(words) > max_tokens else text

# Clean and deduplicate answer
def bulletify(text):
    seen = set()
    cleaned = []
    text = text.replace("•", "").replace(" -", ":")
    lines = re.split(r'(?<=[.!?])\s+', text.strip())
    for line in lines:
        line_clean = re.sub(r"\s+", " ", line.strip())
        if len(line_clean) > 3:
            hash_key = re.sub(r'\W+', '', line_clean.lower())
            if hash_key not in seen:
                cleaned.append(f"• {line_clean}")
                seen.add(hash_key)
    return "\n".join(cleaned)

# Extract top context snippets
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

    docs = retriever.invoke(query)
    if not docs or all(len(doc.page_content.strip()) < 30 for doc in docs):
        return jsonify({"answer": "This question is out of context"})

    context_raw = extract_clean_snippets(docs)
    context = truncate_text(context_raw)

    if len(context.strip()) < 30:
        return jsonify({"answer": "This question is out of context"})

    result = qa_chain.invoke({"query": query, "context": context})
    answer_raw = result.get("result") or result.get("answer") or ""

    # Bulletify and clean
    answer = bulletify(answer_raw)

    # If LLM failed to extract real answer
    out_of_context_phrases = [
        "no specific answer is found",
        "does not provide information",
        "not available in the context",
        "Sorry, I couldn't generate",
        "no relevant information",
        "this question is out of context",
        "bharatgpt is an expert in"
    ]
    if any(phrase in answer.lower() for phrase in out_of_context_phrases):
       return jsonify({"answer": "This question is out of context"})
       

    return jsonify({
        "answer": f"{answer}\n\n📄 Context Snippets:\n{context}"
    })

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000")
    app.run(port=5000)
