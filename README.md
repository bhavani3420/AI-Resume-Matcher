# AI Resume Matcher 🚀

An AI-powered Resume ATS Analyzer built using FastAPI, NLP, Sentence Transformers, and Semantic Similarity.

## Features

- Resume PDF Parsing
- Skill Extraction
- Job Description Analysis
- Semantic Matching using Sentence Transformers
- Hybrid ATS Scoring
- FastAPI Backend
- Dynamic Resume Upload API
- Swagger API Documentation

---

## Tech Stack

### Backend
- FastAPI
- Python
- Uvicorn

### AI/NLP
- Sentence Transformers
- PyTorch
- Scikit-learn
- pdfplumber
- NLP techniques

### Frontend (Upcoming)
- React.js

---

## Project Structure

AI-Resume-Matcher/
│
├── backend/
│ ├── main.py
│ └── resume_analyzer.py
│
├── frontend/
├── notebooks/
├── resumes/
├── job_descriptions/
└── README.md

---

## API Endpoints

### GET /

Returns backend running status.

### POST /analyze

Uploads resume PDF and analyzes ATS compatibility.

---

## How to Run

### 1. Clone Repository

```bash
git clone <repo_link>