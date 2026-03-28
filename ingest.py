from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load data
loader = TextLoader("data/sample.txt")
documents = loader.load()

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in FAISS
db = FAISS.from_documents(documents, embeddings)

# Save database locally
db.save_local("vectorstore")

print("✅ Data processed and stored in FAISS!")