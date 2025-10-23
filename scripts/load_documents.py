# scripts/load_documents.py
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_docs(data_path="data", chunk_size=500, overlap=50):
    loader = DirectoryLoader(data_path, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_documents(documents)

    print(f"✅ Loaded {len(documents)} documents, created {len(chunks)} chunks.")
    return chunks
