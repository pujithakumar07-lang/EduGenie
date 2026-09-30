import json
import re

from ai_client import generate_ai_response


def _extract_json(text: str):
    """Extract JSON from an AI response."""
    text = text.strip()

    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("AI did not return valid JSON.")

    return json.loads(text[start:end + 1])


def generate_quiz(topic: str, level: str = "Beginner") -> dict:
    prompt = f"""
Create a multiple-choice quiz for a {level} student.

Topic:
{topic}

Create exactly 3 questions.

Each question must have exactly 4 different options.

Return ONLY valid JSON in this format:

{{
  "title": "Quiz about {topic}",
  "questions": [
    {{
      "question": "Question text",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "correct_answer": 0,
      "explanation": "Short explanation"
    }}
  ]
}}

Rules:
- correct_answer must be 0, 1, 2, or 3.
- Do not use markdown.
- Do not add text outside the JSON.
"""

    response = generate_ai_response(prompt)
    quiz = _extract_json(response)

    if "questions" not in quiz:
        raise ValueError("Quiz response does not contain questions.")

    if len(quiz["questions"]) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for question in quiz["questions"]:
        if len(question.get("options", [])) != 4:
            raise ValueError("Each question must have exactly 4 options.")

        correct_answer = question.get("correct_answer")

        if correct_answer not in [0, 1, 2, 3]:
            raise ValueError("Invalid correct answer index.")

    return quiz