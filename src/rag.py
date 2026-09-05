from vector_store import search
from llm import generate_answer


def ask(question):
    results = search(
        question,
        top_k=3,
    )

    if not results:
        return "I couldn't find relevant information in the documents."

    context = "\n\n".join(
        result["document"]
        for result in results
    )

    answer = generate_answer(
        question,
        context,
    )

    return answer
