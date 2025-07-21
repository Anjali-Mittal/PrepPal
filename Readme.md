# PrepPal

PrepPal is an intelligent chatbot designed to help students prepare for Computer Science interviews. It uses semantic search and Retrieval Augmented Generation (RAG) techniques to retrieve relevant theory answers from a curated database of CS subjects.

## Features

* 📚 Answers questions from core CS subjects using document embeddings.
* 🔍 Semantic search to find conceptually similar matches instead of keyword matching.
* ⚡ Reduces latency by \~30% by querying only the most relevant document chunks.
* ✅ Avoids hallucinations with fallback logic when no relevant context is retrieved.
* 🧠 Uses local LLMs via [Ollama](https://ollama.com/) for secure and offline inference.
* 🖥️ Simple terminal-based interface for distraction-free interaction.
* 🔄 Easily extensible to new subjects - just add new notes and regenerate embeddings.
* 💬 Automatically formats JSON-based context to produce natural English answers.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Anjali-Mittal/PrepPal.git
cd PrepPal
```

### 2. Install dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 3. Install Ollama

Download and install Ollama (if not already installed) from [https://ollama.com](https://ollama.com)
Make sure it's running in the background.

### 4. Pull a supported model

For example, to use `phi3` locally:

```bash
ollama pull phi3
```

You can change this in the code by setting a different model name in `PrepPal.py`.

### 5. Run PrepPal

On Windows, just double-click:

```
start_PrepPal.bat
```

Or manually run:

```bash
python PrepPal.py
```

---

## 📂 Directory Structure

```
PrepPal/
├── embeddings/             # Stores generated embeddings (auto-created)
├── prepare_db.py           # Add embeddings to DB
├── PrepPal.py              # Main entry point
├── utils.py                # Config for model, DB, and context source
├── start_PrepPal.bat       # Windows launcher
├── requirements.txt
└── README.md
```

---

## 📌 Notes

* **No internet required** after setup - everything runs locally.
* You can add more `.txt` files to '`prepare_db.py'` and rerun embedding generation to update the knowledge base.
* Currently supports **only English** text.
* Designed for factual Q&A, not opinion-based or coding problems.

---
