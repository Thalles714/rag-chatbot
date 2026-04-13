from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

DATA_PATH = "data/documentos"
DB_PATH = "db"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    return documents


def create_database():
    docs = load_documents()
    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(docs, embeddings, persist_directory=DB_PATH)
    db.persist()

    print("✅ Banco vetorial criado com sucesso!")


if __name__ == "__main__":
    create_database()