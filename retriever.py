from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_embedding():
    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings

def create_vector_store(chunks):

    embeddings=create_embedding()

    vector_store=FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    vector_store.save_local("vectorstore/faiss_index")
    return vector_store

def load_vector_store():
    embeddings=create_embedding()

    vector_store=FAISS.load_local(
        "vectorstore/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store

def get_retriever(vector_store):
    retriever=vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )
    return retriever