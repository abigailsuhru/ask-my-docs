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


def search(query, top_k=3):

    query_embedding = model.encode(
        [query]
    )

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
    )

    return results