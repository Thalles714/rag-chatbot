# 🤖 RAG Chatbot com LangChain

Projeto de chatbot utilizando RAG (Retrieval-Augmented Generation) para responder perguntas com base em documentos.

## 🚀 Tecnologias
- LangChain
- OpenAI
- ChromaDB

## 📂 Estrutura
- `src/rag`: lógica principal do RAG
- `scripts`: criação do banco vetorial
- `data`: documentos base

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python scripts/build_database.py
python app.py