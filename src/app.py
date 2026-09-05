import streamlit as st
from pathlib import Path

from chunker import chunk_text
from embeddings import create_embeddings, search


st.title("📚 Ask My Docs")

st.write(
    "Ask a question about your Kubernetes documentation."
)


# Load document
document_path = Path("documents/kubernetes.txt")

text = document_path.read_text(encoding="utf-8")


# Create chunks
chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20,
)


# Create embeddings
embeddings = create_embeddings(chunks)


# User input
query = st.text_input(
    "Ask a question:"
)


if st.button("Ask"):
    if query:
        results = search(
            query,
            chunks,
            embeddings,
            top_k=3,
        )

        st.subheader("Retrieved information")

        for i, result in enumerate(results, start=1):

            st.write(
                f"### Result {i}"
            )

            st.write(
                f"Similarity score: "
                f"{result['score']:.4f}"
            )

            st.write(
                result["chunk"]
            )

            st.divider()

    else:
        st.warning(
            "Please enter a question."
        )