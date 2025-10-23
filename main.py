from scripts.qa_agent import ask_question

if __name__ == "__main__":
    while True:
        question = input("Ask a question (or 'exit'): ")
        if question.lower() == "exit":
            break
        print(ask_question(question))
