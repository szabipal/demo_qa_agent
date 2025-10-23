# app.py
import streamlit as st
from scripts.load_documents import load_and_chunk_docs
from scripts.embed_and_index import create_or_load_index
from scripts.qa_agent import build_qa_agent, ask_question
import os

st.set_page_config(page_title="FLA Exam Assistant", page_icon="🎓", layout="centered")

# --- Header ---
st.markdown("<h1 style='text-align:center; color:#2B547E;'>🎓 FLA Exam Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Your intelligent assistant for First Language Acquisition preparation.</p>", unsafe_allow_html=True)
st.divider()

# --- Session State ---
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Initialize RAG system ---
if st.button("🔄 Initialize / Refresh Knowledge Base"):
    with st.spinner("Building knowledge base..."):
        chunks = load_and_chunk_docs(data_path="data")
        create_or_load_index(chunks)
        st.session_state.qa_chain = build_qa_agent()
    st.success("✅ Knowledge base ready! You can start chatting below.")

# --- Chat Interface ---
if st.session_state.qa_chain:
    user_input = st.chat_input("Ask me a question about your exam materials...")
    if user_input:
        st.session_state.messages.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_question(st.session_state.qa_chain, user_input)
                st.markdown(answer)
                st.session_state.messages.append(("assistant", answer))
else:
    st.info("Click **'Initialize / Refresh Knowledge Base'** to load your study materials.")

# --- Display Chat History ---
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)
