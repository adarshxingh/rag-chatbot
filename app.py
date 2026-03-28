import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

st.title("Smart AI Chatbot 🤖 (RAG + Fallback AI)")

query = st.text_input("Ask something:")

if query:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Load FAISS DB
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Search similar docs
    docs = db.similarity_search(query)

    # Extract context
    context = " ".join([doc.page_content for doc in docs])

    # Load AI model
    generator = pipeline("text-generation", model="gpt2")

    # 🔥 CONDITION: If no useful context → fallback
    if len(context.strip()) < 20:
        prompt = f"""
        Answer this question clearly:

        Question: {query}

        Answer:
        """
    else:
        prompt = f"""
        Answer the question based on context:

        Context: {context}

        Question: {query}

        Answer:
        """

    result = generator(prompt, max_length=150, num_return_sequences=1)

    st.write("🤖 AI Answer:")
    st.write(result[0]["generated_text"])  
