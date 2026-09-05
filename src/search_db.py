from vector_store import search

query = input("Ask a question: ")

results = search(query, top_k=3)

print(f"\nQuestion: {query}\n")

for i, result in enumerate(results, start=1):
    print(f"--- RESULT {i} ---")
    print(f"Distance: {result['distance']:.4f}")
    print(f"Source: {result['metadata']['source']}")
    print(f"Chunk: {result['metadata']['chunk_id']}")
    print(f"Document: {result['document']}")
    print()