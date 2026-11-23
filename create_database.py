
import os

from ingestion import load_documents, split_documents
from retriever import create_vector_store

# 1. Load PDF documents
documents = load_documents("data")

print("Total documents:", len(documents))

# 2. Split documents into chunks
chunks = split_documents(documents)

print("Total chunks:", len(chunks))

# 3. Create vector database
os.makedirs("vectorstore", exist_ok=True)

vector_store=create_vector_store(chunks)

print("FAISS database created successfully!")
