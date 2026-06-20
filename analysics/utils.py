

skills_db = [
    "python",
    "django",
    "sql",
    "mysql",
    "react",
    "javascript",
    "docker",
    "aws",
    "html",
    "css",
    "bootstrap",
    "talwindcss",
]

def find_skills(text):

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found

def calculate_score(skills):

    total = len(skills_db)

    found = len(skills)

    return int((found / total) * 100)

def get_missing_skills(skills):

    missing = []

    for skill in skills_db:

        if skill not in skills:
            missing.append(skill)

    return missing

from PyPDF2 import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text