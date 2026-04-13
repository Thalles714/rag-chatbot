from langchain_openai import ChatOpenAI


def generate_answer(prompt):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3
    )

    response = llm.invoke(prompt)
    return response.content