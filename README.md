```
💬 BharatGPT — Your Indian Market Mentor 🤖  
📘 PDF-based AI Chatbot for Entering the Indian Biomaterials & Sustainability Market

---

🧠 TECH STACK

• FLAN-T5 Small (Hugging Face)  
• LangChain  
• FAISS (vector similarity search)  
• Flask (Python web server)  
• HTML + CSS + JS (Frontend)  
• Local LLM-ready (TinyLLaMA GGUF) — optional

---

✅ Works on local machines (Windows-friendly). Requires Python and pip.

---

📁 PROJECT SETUP — STEP-BY-STEP

▶️ STEP 1: Clone or unzip the project folder

1. Place the file `sustainable_biomaterials_india.pdf` (or your own PDF) inside the root folder.  
2. Open terminal (CMD or PowerShell) inside the project folder.

▶️ STEP 2: Install dependencies, process PDF, and launch the chatbot

Run the following commands **in order**:

pip install -r requirements.txt  
python process_pdf.py  
python app.py  

You should see:

Running on http://127.0.0.1:5000

Then, open your browser and visit:  
👉 http://localhost:5000

You can now ask questions like:

• "How to enter the Indian sustainability market?"  
• "What are regulatory challenges for biomaterials in India?"  
• "How to apply for BIRAC support?"  
• "How to lead the Indian market in sustainable biomaterials?"  

---

✨ Optional: Use Local LLM with `.gguf` model (Advanced)

If you want to run an open-source LLM locally without internet (e.g. TinyLLaMA):

1. Download a `.gguf` model from Hugging Face:  
   🔗 https://huggingface.co/cmp-nct/TinyLlama-1.1B-Chat-v1.0-GGUF

2. Rename the file to:

model.gguf

3. Place it inside:

ai_pdf_chatbot_prebuilt/models/

4. Run it using `llama.cpp`, `llama-cpp-python`, or `Ollama` as backend.  
   _(Note: this project currently uses FLAN-T5 by default)_

---

🧪 Test with cURL (optional)

curl -X POST http://localhost:5000/chat \  
     -H "Content-Type: application/json" \  
     -d "{\"message\": \"How to dominate the Indian biomaterials market?\"}"

If you see a valid answer in response — ✅ YOU DID IT!

---

👨‍💻 Credits

Created by: Penke Sreeram Kasulu  
Powered by: Open-Source AI & Indian Market Research 💡  
License: MIT
```
