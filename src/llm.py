from ollama import chat


def generate_answer(question, context):
    prompt = f"""
You are a helpful document question-answering assistant.

Answer the user's question using ONLY the information provided
in the context below.

Do not use outside knowledge.

If the answer cannot be found in the context, say:
"I couldn't find the answer in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]