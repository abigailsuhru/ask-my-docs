from vector_store import collection


print("Number of documents:")
print(collection.count())


results = collection.get(
    include=["documents", "metadatas"]
)


for i, document in enumerate(
    results["documents"]
):

    print("\n--------------------")

    print(
        f"Document: {document}"
    )

    print(
        f"Metadata: {results['metadatas'][i]}"
    )