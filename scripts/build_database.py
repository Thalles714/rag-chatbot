from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/documentos"
DB_PATH = ROOT / "db"


def load_documents():
    if not DATA_PATH.is_dir():
        raise FileNotFoundError(f"Crie {DATA_PATH} e adicione seus PDFs autorizados.")
    documents = []
    for file in sorted(DATA_PATH.glob("*.pdf")):
        documents.extend(PyPDFLoader(str(file)).load())
    if not documents:
        raise ValueError("Nenhum documento PDF com páginas foi encontrado.")
    return documents


def create_database():
    load_dotenv(ROOT / ".env")
    # Evita duplicar o corpus e cobrar embeddings novamente por engano.
    if DB_PATH.exists() and any(DB_PATH.iterdir()):
        raise FileExistsError("O índice db/ já existe. Remova-o manualmente para reindexar.")
    docs = load_documents()
    Chroma.from_documents(docs, OpenAIEmbeddings(), persist_directory=str(DB_PATH))
    # Chroma persiste automaticamente ao receber persist_directory.
    print("Banco vetorial criado com sucesso!")


if __name__ == "__main__":
    create_database()
