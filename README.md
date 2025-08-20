# 💬 BharatGPT — Your Indian Market Mentor 🤖  
**AI PDF Chatbot for Biomaterials, Sustainability, and Circular Economy in India**  
**Live Demo:** [https://bharatgpt-indian-market-mentor.streamlit.app/](https://bharatgpt-indian-market-mentor.streamlit.app/)

---

## 🧠 TECH STACK

- **FLAN-T5 Small (`MBZUAI/LaMini-Flan-T5-248M`)** – Compact, fast, and accurate  
- **LangChain** – Intelligent chaining and prompt handling  
- **FAISS** – Vector similarity search over PDFs  
- **Flask** – Lightweight web server  
- **HTML + CSS + JS** – Front-end UI  
- **Runs on CPU** – No GPU required  

---

## ✅ Fully Local — Works on Windows, macOS, Linux  
Requires **Python 3.9+** and `pip`

---

## 📁 Project Setup

### ▶️ STEP 1: Setup Project Directory

1. Clone or unzip the project folder  
2. Add your PDF (e.g. `biomaterials_india.pdf`) to the root directory  
3. Open a terminal in the project folder  

---

### ▶️ STEP 2: Install Requirements & Start Server

```bash
pip install -r requirements.txt
python process_pdf.py     # Convert PDF to vectorstore
python app.py             # Launch the chatbot
```

Your browser will open at:  
👉 http://localhost:5000

---

## 💬 What Can You Ask?

Ask BharatGPT about:

- 📦 India’s rules for biodegradable packaging  
- 🏭 Setting up a recycling facility with ULBs  
- 📊 Government schemes for sustainability startups  
- 🧪 Partnering with IISc, CSIR, or BIRAC  
- 💡 Examples like MYNUSCo, Recykal, or BioE3 Policy  

Out-of-context questions (e.g., "Who is Virat Kohli?") will return:  
> **"This question is out of context"**

---

## 🧪 Test via `curl` (Optional)

```bash
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d "{\"message\": \"How to expand my startup in Indian market?\"}"
```

---

## 📌 Features Recap

| Feature                             | Status     |
|-------------------------------------|------------|
| 🧠 PDF‑trained LLM with FAISS        | ✅ Enabled |
| 📍 Bullet‑point answers (no repeats) | ✅ Clean   |
| 🚫 Rejects out‑of-context questions  | ✅ Working |
| ⚡ Fast inference (<3 sec CPU)       | ✅ OK      |
| 📄 Shows helpful context snippets    | ✅ Smart   |

---

## 🔒 Optional: Local `.gguf` LLM Support

To run a local LLM via `llama.cpp`, follow these steps:

1. Download the `.gguf` model file, e.g.:  
   `TinyLlama-1.1B-Chat-v1.0-GGUF` from Hugging Face  
2. Rename it to `model.gguf`  
3. Place it in the `/models/` directory  
4. Load it using `llama-cpp-python`, `Ollama`, or similar tools

---

## 👨‍💻 Author

**Made by:** Penke Sreeram Kasulu  
**Mission:** Help the world navigate the Indian sustainability market with AI 🌱
