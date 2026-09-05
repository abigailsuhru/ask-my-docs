from pathlib import Path

from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import collection


document_path = Path("documents/kubernetes.txt")

text = document_path.read_text(
    encoding="utf-8"
)

chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20,
)

embeddings = create_embeddings(chunks)


ids = [
    f"kubernetes-{i}"
    for i in range(len(chunks))
]


metadatas = [
    {
        "source": document_path.name,
        "chunk_id": i,
    }
    for i in range(len(chunks))
]


collection.upsert(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist(),
    metadatas=metadatas,
)


print(
    f"Stored {len(chunks)} chunks in ChromaDB."
)