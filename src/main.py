from pathlib import Path

from chunker import chunk_text
from embeddings import create_embeddings, search


document_path = Path("documents/kubernetes.txt")

text = document_path.read_text(encoding="utf-8")

chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20,
)

embeddings = create_embeddings(chunks)

query = input("Ask a question: ")

results = search(
    query,
    chunks,
    embeddings,
    top_k=3,
)

print(f"\nQuestion: {query}\n")

for i, result in enumerate(results, start=1):
    print(f"--- RESULT {i} ---")
    print(f"Score: {result['score']:.4f}")
    print(result["chunk"])
    print()