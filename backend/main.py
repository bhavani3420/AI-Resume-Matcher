from fastapi import FastAPI

from backend.resume_analyzer import analyze_resume

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Resume Matcher Backend Running"
    }


@app.post("/analyze")
def analyze():

    result = analyze_resume()

    return result