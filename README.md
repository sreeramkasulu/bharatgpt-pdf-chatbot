# 💬 BharatGPT — Your Indian Market Mentor 🤖  
**PDF-based AI Chatbot for Entering the Indian Biomaterials & Sustainability Market**

---

## 🧠 TECH STACK

- **FLAN-T5 Small** (Hugging Face)  
- **LangChain**  
- **FAISS** (vector similarity search)  
- **Flask** (Python web server)  
- **HTML + CSS + JS** (Frontend)  
- **Local LLM-ready** (TinyLLaMA `.gguf`) — optional

---

## ✅ Works locally on Windows/macOS/Linux  
Requires Python 3.9+ and `pip`

---

## 📁 Project Setup — Step-by-Step

### ▶️ STEP 1: Prepare your project

1. Clone or unzip the project folder  
2. Place your PDF (e.g. `sustainable_biomaterials_india.pdf`) in the root directory  
3. Open terminal in the project folder  

---

### ▶️ STEP 2: Install & Launch

```bash
pip install -r requirements.txt
python process_pdf.py
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

Then open your browser:  
👉 http://localhost:5000

---

You can now ask questions like:

- "How to enter the Indian sustainability market?"  
- "What are regulatory challenges for biomaterials in India?"  
- "How to apply for BIRAC support?"  
- "How to lead the Indian market in sustainable biomaterials?"  

---

## ✨ Optional: Use Local LLM with `.gguf` model (Advanced)

If you want to run an LLM offline using TinyLLaMA:

1. Download from Hugging Face:  
   👉 https://huggingface.co/cmp-nct/TinyLlama-1.1B-Chat-v1.0-GGUF

2. Rename the file to:
   ```
   model.gguf
   ```

3. Place it here:
   ```
   ai_pdf_chatbot_prebuilt/models/
   ```

4. Run it using `llama.cpp`, `llama-cpp-python`, or `Ollama`  
   ⚠️ FLAN-T5 is used by default

---

## 🧪 Test with curl (optional)

```bash
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d "{\"message\": \"How to dominate the Indian biomaterials market?\"}"
```

✅ If you get a valid answer — YOU DID IT!

---

## 👨‍💻 Credits

**Created by:** Penke Sreeram Kasulu  
**Powered by:** Open-Source AI & Indian Market Research 💡  

