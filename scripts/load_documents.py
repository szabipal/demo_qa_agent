# scripts/load_documents.py
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

def load_and_chunk_docs(data_path="data", chunk_size=500, overlap=50):
    data_dir = Path(data_path)
    documents = []

    # --- Load .txt files recursively ---
    txt_loader = DirectoryLoader(str(data_dir), glob="**/*.txt", loader_cls=TextLoader)
    txt_docs = txt_loader.load()
    documents.extend(txt_docs)

    # --- Load .pdf files recursively ---
    pdf_files = list(data_dir.glob("**/*.pdf"))
    for pdf_file in pdf_files:
        try:
            pdf_loader = PyPDFLoader(str(pdf_file))
            pdf_docs = pdf_loader.load()
            documents.extend(pdf_docs)
        except Exception as e:
            print(f"⚠️ Error reading {pdf_file.name}: {e}")

    if not documents:
        print("⚠️ No documents found in data folder.")
        return []

    # --- Split into chunks for embeddings ---
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_documents(documents)

    print(f"✅ Loaded {len(documents)} documents, created {len(chunks)} chunks.")
    return chunks
