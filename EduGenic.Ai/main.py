
"""EduGenie FastAPI application."""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from ai_client import AIServiceError
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


ROOT = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie",
    version="1.0.0",
    description="AI-powered learning assistant"
)

app.mount(
    "/static",
    StaticFiles(directory=ROOT / "static"),
    name="static"
)

templates = Jinja2Templates(
    directory=str(ROOT / "templates")
)


class TextInput(BaseModel):
    text: str = Field(min_length=2, max_length=20000)


class LearningInput(TextInput):
    level: str = Field(
        default="beginner",
        pattern="^(beginner|intermediate|advanced)$"
    )


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
def health():
    return {"status": "ok"}


def run(fn, *args):
    try:
        return {"result": fn(*args)}
    except AIServiceError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        ) from exc


@app.post("/qa")
def qa(payload: TextInput):
    return run(answer_question, payload.text)


@app.post("/explain")
def explain(payload: TextInput):
    return run(explain_concept, payload.text)


@app.post("/quiz")
def quiz(payload: TextInput):
    return run(generate_quiz, payload.text)


@app.post("/summarize")
def summarize(payload: TextInput):
    return run(summarize_text, payload.text)


@app.post("/learn/recommendations")
def recommendations(payload: LearningInput):
    return run(
        get_learning_recommendations,
        payload.text,
        payload.level
    )