# 🤖 AI Chatbot using RAG (Retrieval-Augmented Generation)

## 📌 Overview

This project is an AI-powered chatbot that answers user queries using a Retrieval-Augmented Generation (RAG) approach. It combines vector search with a language model to provide context-aware responses.

The chatbot retrieves relevant information from stored data and generates intelligent answers. If no relevant data is found, it falls back to a general AI response.

---

## 🚀 Features

* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware AI responses
* 🔁 Fallback to general AI when no data is found
* 💻 Simple web interface using Streamlit
* ⚡ Fast local execution (no API key required)

---

## 🏗️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* HuggingFace Embeddings
* Transformers (GPT-2)
* Streamlit

---

## 🧠 How It Works (RAG Pipeline)

1. 📄 Load documents from text file
2. 🔢 Convert text into embeddings
3. 🗄️ Store embeddings in FAISS vector database
4. 🔍 Retrieve relevant data based on user query
5. 🤖 Generate response using AI model
6. 🔁 Fallback to general AI if no relevant context

---

## 📂 Project Structure

```
rag-chatbot/
│── app.py              # Chatbot UI
│── ingest.py           # Data processing & vector storage
│── data/
│     └── sample.txt    # Input data
│── vectorstore/        # Stored embeddings
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Process Data

```
python ingest.py
```

### Step 2: Run Chatbot

```
python -m streamlit run app.py
```

---

## 💡 Example Queries

* What is Artificial Intelligence?
* Explain Machine Learning
* Suggest me names

---

## 🔄 Role of Vector Database

This project uses **FAISS** for local vector storage and similarity search.

👉 In production systems, scalable vector databases like **Endee** can be used for:

* Large-scale data storage
* Faster semantic search
* Distributed AI systems

---

## 📈 Future Improvements

* Integrate Endee vector database
* Use advanced LLMs (LLaMA / Mistral)
* Add PDF and multi-file support
* Improve UI/UX

---

## 🤝 Contributing

Feel free to fork this repository and improve it.

---

## 📌 Author

Adarsh Singh
BTech CSE | AI/ML Enthusiast

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
