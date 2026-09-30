import os

from dotenv import load_dotenv
from google import genai


# Load environment variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Use the model from .env if provided.
# Otherwise use the current model.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


class AIServiceError(Exception):
    """Raised when the Gemini AI service cannot generate a response."""


# Create Gemini client only when an API key is available
if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY":
    client = None
else:
    client = genai.Client(api_key=GEMINI_API_KEY)


def generate_ai_response(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the generated response.
    """

    if client is None:
        raise AIServiceError(
            "Gemini API key is missing. "
            "Please add GEMINI_API_KEY to the .env file."
        )

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        if not response or not response.text:
            raise AIServiceError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as exc:
        raise AIServiceError(
            f"Gemini API error: {exc}"
        ) from exc