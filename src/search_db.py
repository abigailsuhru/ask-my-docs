from vector_store import search


query = input("Ask a question: ")


results = search(
    query,
    top_k=3,
)


print(
    f"\nQuestion: {query}\n"
)


if not results:

    print(
        "I couldn't find relevant information "
        "in the documents."
    )

else:

    for i, result in enumerate(
        results,
        start=1,
    ):

        print(
            f"--- RESULT {i} ---"
        )

        print(
            f"Distance: "
            f"{result['distance']:.4f}"
        )

        print(
            f"Source: "
            f"{result['metadata']['source']}"
        )

        print(
            f"Chunk: "
            f"{result['metadata']['chunk_id']}"
        )

        print(
            result["document"]
        )

        print()