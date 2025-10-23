# main.py
from scripts.load_documents import load_and_chunk_docs
from scripts.embed_and_index import create_or_load_index
from scripts.qa_agent import build_qa_agent, ask_question
import os

if __name__ == "__main__":
    print("🔧 Preparing your QA system...")

    if not os.path.exists("vector_store"):
        chunks = load_and_chunk_docs(data_path="data")
        create_or_load_index(chunks)

    qa_chain = build_qa_agent()
    print("✅ Ready! Ask me anything about your documents.")

    while True:
        question = input("\n❓ Question (or 'exit'): ")
        if question.lower() == "exit":
            break
        print("💬", ask_question(qa_chain, question))
