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

    if not query:

        st.warning(
            "Please enter a question."
        )

    else:

        results = search(
            query,
            top_k=3,
        )

        if not results:

            st.warning(
                "I couldn't find relevant "
                "information in the documents."
            )

        else:

            st.subheader(
                "Retrieved information"
            )

            for i, result in enumerate(
                results,
                start=1,
            ):

                st.write(
                    f"### Result {i}"
                )

                st.write(
                    f"Distance: "
                    f"{result['distance']:.4f}"
                )

                st.write(
                    f"Source: "
                    f"{result['metadata']['source']}"
                )

                st.write(
                    f"Chunk: "
                    f"{result['metadata']['chunk_id']}"
                )

                st.write(
                    result["document"]
                )

                st.divider()
