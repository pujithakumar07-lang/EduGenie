from ai_client import generate_ai_response


def get_learning_recommendations(topic: str, level: str = "Beginner") -> str:
    prompt = f"""
You are EduGenie, an educational learning assistant.

Create a learning roadmap for the topic below.

Topic:
{topic}

Current level:
{level}

Include:
1. Beginner concepts
2. Intermediate concepts
3. Advanced concepts
4. Suggested timeline
5. Practice activities
6. Useful learning resources

Use simple language and organize the roadmap with clear headings and bullet points.
"""

    return generate_ai_response(prompt)