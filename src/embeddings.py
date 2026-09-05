from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    return model.encode(chunks)


def search(query, chunks, embeddings, top_k=3):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings,
    )[0]

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        results.append(
            {
                "chunk": chunks[index],
                "score": similarities[index],
            }
        )

    return results