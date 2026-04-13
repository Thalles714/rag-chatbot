from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

DB_PATH = "db"
TOP_K = 5
THRESHOLD = 0.6


def get_context(query: str):
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

    results = db.similarity_search_with_relevance_scores(query, k=TOP_K)

    if not results or results[0][1] < THRESHOLD:
        return None

    docs = [doc.page_content for doc, _ in results]
    return "\n\n---\n\n".join(docs)