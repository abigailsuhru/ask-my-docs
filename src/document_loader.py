import fitz


def load_document(uploaded_file):
    file_name = uploaded_file.name
    file_type = file_name.lower().split(".")[-1]

    if file_type in ["txt", "md"]:
        text = uploaded_file.read().decode("utf-8")
        return text

    elif file_type == "pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        pages = []

        for page in pdf:
            pages.append(page.get_text())

        return "\n".join(pages)

    else:
        raise ValueError(
            "Unsupported file type. Please upload TXT, MD, or PDF."
        )
