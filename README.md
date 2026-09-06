## Architecture

Ask My Docs is a fully local RAG application.

Steps to run:
1. Make sure git and python are installed 
2. Clone this repo
3. cd ask-my-docs
4. python -m venv .venv
5. .venv\Scripts\Activate.ps1
6. python -m pip install --upgrade pip
7. pip install -r requirements.txt
8. Install ollama - check -> ollama --version
9. ollama pull llama3.2:3b
10. streamlit run src/app.py


```text
Document Upload → Load → Chunk → Embed → ChromaDB
                                          ↓
User Question → Embed → Semantic Search → Relevant Chunks
                                          ↓
                                   Ollama / Llama 3.2
                                          ↓
                                     Final Answer
                                          ↓
                                      Streamlit


                         ASK MY DOCS
                              │
             ┌────────────────┴────────────────┐
             │                                 │
       Document Upload                    User Question
       PDF / TXT / MD                          │
             │                                 │
             ▼                                 ▼
      Document Loader                  Sentence Transformer
             │                                 │
             ▼                                 ▼
          Chunking                         Query Embedding
             │                                 │
             ▼                                 │
      Sentence Transformer                       │
             │                                 │
             ▼                                 │
         Embeddings                             │
             │                                 │
             └──────────────┐    ┌─────────────┘
                            ▼    ▼
                         ChromaDB
                       Vector Search
                            │
                            ▼
                     Relevant Chunks
                            │
                            ▼
                    Ollama / Llama 3.2
                            │
                            ▼
                       Final Answer
                            │
                            ▼
                        Streamlit


                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               │ Upload document
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │     Web Interface    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Document Loader     │
                    │   PDF / TXT / MD     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Chunking        │
                    │   100 words / 20     │
                    │      overlap         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Sentence           │
                    │  Transformer        │
                    │ all-MiniLM-L6-v2     │
                    └──────────┬───────────┘
                               │
                               │ Embeddings
                               ▼
                    ┌──────────────────────┐
                    │      ChromaDB        │
                    │   Vector Database    │
                    │                      │
                    │ Document + Embedding │
                    │      + Metadata      │
                    └──────────┬───────────┘
                               │
                               │ User question
                               ▼
                    ┌──────────────────────┐
                    │   Semantic Search    │
                    │      Top-K chunks    │
                    └──────────┬───────────┘
                               │
                               │ Relevant context
                               ▼
                    ┌──────────────────────┐
                    │       Ollama         │
                    │     Llama 3.2 3B     │
                    │      Local LLM       │
                    └──────────┬───────────┘
                               │
                               │ Generated answer
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │    Final Answer      │
                    └──────────────────────┘



| Component        | Technology            |
| ---------------- | --------------------- |
| UI               | Streamlit             |
| Document parsing | PyMuPDF               |
| Chunking         | Python                |
| Embeddings       | Sentence Transformers |
| Vector database  | ChromaDB              |
| LLM              | Ollama + Llama 3.2 3B |
| Language         | Python                |
| Cost             | $0 / Local            |
