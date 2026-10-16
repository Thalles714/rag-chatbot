from pathlib import Path

from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

DB_PATH = Path(__file__).resolve().parents[2] / "db"
TOP_K = 5
THRESHOLD = 0.6


def get_context(query: str):
    if not DB_PATH.is_dir() or not any(DB_PATH.iterdir()):
        raise FileNotFoundError("Índice ausente. Execute python -m scripts.build_database primeiro.")
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory=str(DB_PATH), embedding_function=embeddings)
    results = db.similarity_search_with_relevance_scores(query, k=TOP_K)
    docs = [doc.page_content for doc, score in results if score >= THRESHOLD]
    return "\n\n---\n\n".join(docs) if docs else None
