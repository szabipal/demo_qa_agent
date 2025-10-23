# # scripts/qa_agent.py
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

def build_qa_agent(index_path="vector_store"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        index_path, embeddings, allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    prompt = ChatPromptTemplate.from_template(
        "Answer the question using the context below.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )

    # LCEL-style retrieval-augmented chain
    qa_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    print("🤖 QA agent ready (LCEL pipeline).")
    return qa_chain


def ask_question(qa_chain, question):
    result = qa_chain.invoke(question)
    return result.content
