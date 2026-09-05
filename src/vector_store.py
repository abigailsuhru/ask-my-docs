import chromadb

from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="chroma_db"
)


collection = client.get_or_create_collection(
    name="documents"
)


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def search(query, top_k=3, max_distance=0.85):
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
    )

    documents = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    filtered_results = []

    for document, distance, metadata in zip(
        documents,
        distances,
        metadatas,
    ):
        if distance <= max_distance:
            filtered_results.append(
                {
                    "document": document,
                    "distance": distance,
                    "metadata": metadata,
                }
            )

    return filtered_results