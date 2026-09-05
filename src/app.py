import streamlit as st

from rag import ask


st.set_page_config(
    page_title="Ask My Docs",
    page_icon="📚",
)

st.title("📚 Ask My Docs")
st.write("Ask a question about your Kubernetes documentation.")

query = st.text_input("Ask a question:")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            answer = ask(query)

        st.subheader("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question.")
