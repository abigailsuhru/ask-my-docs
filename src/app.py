import streamlit as st

from vector_store import search


st.title("📚 Ask My Docs")

st.write(
    "Ask a question about your Kubernetes documentation."
)


query = st.text_input(
    "Ask a question:"
)


if st.button("Ask"):

    if query:

        results = search(
            query,
            top_k=3,
        )

        st.subheader(
            "Retrieved information"
        )

        for i, document in enumerate(
            results["documents"][0],
            start=1,
        ):

            distance = results["distances"][0][i - 1]

            st.write(
                f"### Result {i}"
            )

            st.write(
                f"Distance: {distance:.4f}"
            )

            st.write(document)

            st.divider()

    else:

        st.warning(
            "Please enter a question."
        )