from ai_client import generate_ai_response


def explain_concept(topic: str, level: str = "Beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic for a {level} student.

Topic:
{topic}

Instructions:
- Start with a simple definition.
- Explain the concept clearly.
- Use simple language.
- Give a practical example.
- Include important points.
- Avoid unnecessary technical complexity.
"""

    return generate_ai_response(prompt)