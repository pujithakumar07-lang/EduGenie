from ai_client import generate_ai_response


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following text clearly for a college student.

Text:
{text}

Instructions:
- Give a short summary.
- Identify the main ideas.
- Use simple language.
- Use bullet points for important points.
- Do not add information that is not present in the text.
"""

    return generate_ai_response(prompt)