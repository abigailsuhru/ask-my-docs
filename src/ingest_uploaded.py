from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import collection


def ingest_document(text, source):
    chunks = chunk_text(
        text,
        chunk_size=100,
        overlap=20,
    )

    embeddings = create_embeddings(chunks)

    ids = [
        f"{source}-{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "source": source,
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

    return len(chunks)
