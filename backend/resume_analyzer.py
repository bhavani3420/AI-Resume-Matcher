import pdfplumber
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


skills_db = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "react",
    "node.js",
    "mongodb",
    "mysql",
    "django",
    "fastapi",
    "docker",
    "aws",
    "html",
    "css",
    "git",
    "github"
]


model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(pdf_path):

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text.lower()


def extract_skills(text):

    tokens = re.findall(r"\b\w[\w.+#-]*\b", text)

    extracted_skills = []

    for skill in skills_db:

        if skill in tokens:
            extracted_skills.append(skill)

    return list(set(extracted_skills))


def calculate_similarity(resume_text, jd_text):

    embeddings = model.encode([resume_text, jd_text])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return  float(round(similarity * 100, 2))

def analyze_resume():

    resume_path = "resumes/resume.pdf"

    jd_text = """
    Looking for Python developer with FastAPI,
    Docker, AWS, MongoDB and React skills.
    """

    resume_text = extract_text_from_pdf(resume_path)

    extracted_skills = extract_skills(resume_text)

    matched_skills = []

    missing_skills = []

    jd_lower = jd_text.lower()

    for skill in skills_db:

        if skill in jd_lower:

            if skill in extracted_skills:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

    keyword_score = (
        len(matched_skills) /
        (len(matched_skills) + len(missing_skills))
    ) * 100

    semantic_score = calculate_similarity(
        resume_text,
        jd_text
    )

    final_score = (
        keyword_score * 0.4 +
        semantic_score * 0.6
    )

    result = {
        "keyword_score": round(keyword_score, 2),
        "semantic_score": round(semantic_score, 2),
        "final_score": round(final_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    return result