def log_interaction(question, answer):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"Pergunta: {question}\n")
        f.write(f"Resposta: {answer}\n")
        f.write("-" * 50 + "\n")