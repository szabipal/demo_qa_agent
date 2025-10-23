# scripts/embed_and_index.py
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
import os

def create_or_load_index(chunks, index_path="vector_store"):
    os.makedirs(index_path, exist_ok=True)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)
    print(f"✅ Vector index saved to {index_path}")
    return vectorstore
