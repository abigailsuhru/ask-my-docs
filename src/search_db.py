from rag import ask

query = input("Ask a question: ")

answer = ask(query)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)