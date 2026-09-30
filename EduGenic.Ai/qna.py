from ai_client import generate_ai_response


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple language.
- Explain step by step when necessary.
- Give examples when useful.
- Keep the answer suitable for a college student.
"""
