#!/bin/bash

# ====== CONFIGURATION ======
PROJECT_NAME="simple_qa_agent"
PYTHON_VERSION="3.10"  # or change to your preferred version
GITHUB_REPO_URL="https://github.com/szabipal/demo_qa_agent.git"  # <-- CHANGE THIS
# ===========================

echo "🔧 Creating project: $PROJECT_NAME"
mkdir $PROJECT_NAME && cd $PROJECT_NAME

echo "🐍 Setting up Python virtual environment"
python$PYTHON_VERSION -m venv venv
source venv/bin/activate

echo "📦 Installing dependencies"
pip install --upgrade pip
pip install langchain openai faiss-cpu tiktoken unstructured streamlit

echo "🗃️ Creating project structure"
mkdir data scripts
touch .env .gitignore README.md
touch scripts/load_documents.py
touch scripts/embed_and_index.py
touch scripts/qa_agent.py
touch main.py

echo "📝 Writing boilerplate files"

# .gitignore
cat <<EOL > .gitignore
venv/
__pycache__/
.env
EOL

# README.md
cat <<EOL > README.md
# Simple QA Agent

A basic Retrieval-Augmented Generation (RAG) based question-answering system using LangChain and OpenAI.

## Setup

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Run
\`\`\`bash
python main.py
\`\`\`
EOL

# requirements.txt
pip freeze > requirements.txt

# Minimal main.py
cat <<EOL > main.py
from scripts.qa_agent import ask_question

if __name__ == "__main__":
    while True:
        question = input("Ask a question (or 'exit'): ")
        if question.lower() == "exit":
            break
        print(ask_question(question))
EOL

# Minimal qa_agent.py
cat <<EOL > scripts/qa_agent.py
def ask_question(question):
    # Placeholder
    return "You asked: " + question
EOL

echo "🔗 Initializing Git and pushing to GitHub"
git init
git remote add origin $GITHUB_REPO_URL
git add .
git commit -m "Initial commit: setup QA agent project structure"
git branch -M main
git push -u origin main

echo "✅ Done! Project '$PROJECT_NAME' is ready and connected to GitHub."
