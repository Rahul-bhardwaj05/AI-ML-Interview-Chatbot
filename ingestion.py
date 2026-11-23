from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_documents(data_path):
    documents=[]
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            file_path=os.path.join(data_path,file)

            loader=PyPDFLoader(file_path)
            docs=loader.load()
            documents.extend(docs)
    return documents

def split_documents(documents):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

    chunks=text_splitter.split_documents(documents)

    return chunks