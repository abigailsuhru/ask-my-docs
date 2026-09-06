import streamlit as st

from document_loader import load_document
from ingest_uploaded import ingest_document
from rag import ask


st.set_page_config(
    page_title="Ask My Docs",
    page_icon="📚",
)

st.title("📚 Ask My Docs")

st.write(
    "Upload a document and ask questions about its contents."
)


st.header("1. Upload a document")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "md"],
)


if uploaded_file is not None:

    st.write(f"Selected: **{uploaded_file.name}**")

    if st.button("Ingest document"):

        with st.spinner("Reading and indexing document..."):

            text = load_document(uploaded_file)

            chunk_count = ingest_document(
                text,
                uploaded_file.name,
            )

        st.success(
            f"Document indexed successfully! "
            f"Created {chunk_count} chunks."
        )


st.header("2. Ask a question")

query = st.text_input(
    "What would you like to know?"
)


if st.button("Ask"):

    if query:

        with st.spinner("Thinking..."):

            answer = ask(query)

        st.subheader("Answer")

        st.write(answer)

    else:

        st.warning(
            "Please enter a question."
        )
