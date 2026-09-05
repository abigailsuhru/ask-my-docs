from vector_store import collection


print("Number of documents:")
print(collection.count())


print("\nStored documents:")

results = collection.get()

for document in results["documents"]:
    print("\n---")
    print(document)