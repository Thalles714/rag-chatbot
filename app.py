from pathlib import Path
from dotenv import load_dotenv

from src.rag.retriever import get_context
from src.rag.generator import generate_answer
from src.rag.prompt import build_prompt


def main():
    load_dotenv(Path(__file__).resolve().parent / ".env")
    while True:
        try:
            question = input("\nPergunta (ou 'sair'): ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question:
            continue

        if question.lower() == "sair":
            break

        context = get_context(question)

        if not context:
            print("⚠️ Nenhuma informação encontrada.")
            continue

        prompt = build_prompt(question, context)
        answer = generate_answer(prompt)

        print("\n🤖 Resposta:")
        print(answer)


if __name__ == "__main__":
    main()