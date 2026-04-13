from src.rag.retriever import get_context
from src.rag.generator import generate_answer
from src.rag.prompt import build_prompt


def main():
    while True:
        question = input("\nPergunta (ou 'sair'): ")

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