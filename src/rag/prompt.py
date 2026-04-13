from langchain.prompts import ChatPromptTemplate


def build_prompt(question: str, context: str):
    template = """
Você é um assistente especializado em responder perguntas com base em documentos.

Regras:
- Use apenas o contexto fornecido
- Se não souber, diga claramente
- Seja objetivo

Pergunta:
{question}

Contexto:
{context}

Resposta:
"""
    prompt = ChatPromptTemplate.from_template(template)

    return prompt.invoke({
        "question": question,
        "context": context
    })