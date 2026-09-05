from vector_store import search


query = input("Ask a question: ")


results = search(
    query,
    top_k=3,
)


print(
    f"\nQuestion: {query}\n"
)


for i, document in enumerate(
    results["documents"][0],
    start=1,
):

    distance = results["distances"][0][i - 1]

    print(f"--- RESULT {i} ---")
    print(f"Distance: {distance:.4f}")
    print(document)
    print()