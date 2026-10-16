# RAG Chatbot — protótipo com documentos PDF

Aplicação educacional de terminal para consultar documentos PDF com LangChain, OpenAI e ChromaDB. Recupera páginas acima de um limiar de relevância e gera uma resposta baseada no contexto.

## Preparar

Requer Python 3.11 ou 3.12 e uma chave da API OpenAI. Na raiz do repositório:

```sh
python -m venv .venv
```

Ative o ambiente: Windows `.venv\Scripts\activate`; macOS/Linux `source .venv/bin/activate`. Depois:

```sh
python -m pip install -r requirements.txt
```

Copie `.env.example` para `.env` e informe `OPENAI_API_KEY`. A pasta `data/documentos/` inclui um cardápio de exemplo. Para usar outros PDFs, adicione somente documentos autorizados. Documentos privados, a chave e o índice `db/` não devem ser versionados.

```sh
python -m scripts.build_database
python app.py
```

O `.env`, os PDFs e o índice são localizados a partir do projeto. O Chroma persiste automaticamente. O indexador recusa um `db/` já preenchido para evitar duplicação e cobrança acidental de embeddings; para reindexar, remova conscientemente o índice local e execute de novo.

## Testes offline

```sh
python -m unittest discover -s tests -v
```

Os clientes externos são substituídos nos testes. Não há chamadas pagas. São verificados o limiar por documento, mensagens de sistema/usuário, índice ausente e prevenção de reindexação duplicada.

## Estrutura

- `app.py`: interação pelo terminal.
- `scripts/build_database.py`: leitura de PDFs e criação do índice.
- `src/rag/retriever.py`: recuperação de páginas relevantes.
- `src/rag/prompt.py`: composição das mensagens.
- `src/rag/generator.py`: geração via API.

## Limites

O conteúdo dos PDFs é enviado à OpenAI para embeddings; perguntas e páginas recuperadas são enviados para gerar respostas. As chamadas podem gerar cobrança. Use dados autorizados e configure limites de consumo na conta do provedor.

Este é um protótipo, sem OCR, divisão refinada de páginas, autenticação web ou controle de consumo por usuário. A separação das mensagens e o limiar de relevância não garantem precisão nem resistência completa a prompt injection. Não publique como uma API aberta sem adicionar os controles necessários.
