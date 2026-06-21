# skills_db = [
#     "python",
#     "django",
#     "sql",
#     "mysql",
#     "react",
#     "javascript",
#     "docker",
#     "aws",
#     "html",
#     "css",
#     "bootstrap",
#     "talwindcss",
# ]

# def find_skills(text):

#     found = []

#     text = text.lower()

#     for skill in skills_db:

#         if skill in text:
#             found.append(skill)

#     return found

# def calculate_score(skills):

#     total = len(skills_db)

#     found = len(skills)

#     return int((found / total) * 100)

# def get_missing_skills(skills):

#     missing = []

#     for skill in skills_db:

#         if skill not in skills:
#             missing.append(skill)

#     return missing

# from PyPDF2 import PdfReader

# def extract_text(pdf_path):

#     reader = PdfReader(pdf_path)

#     text = ""

#     for page in reader.pages:

#         text += page.extract_text()

#     return text


from PyPDF2 import PdfReader
import google.generativeai as genai
import json
import re
from django.conf import settings



genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def analyze_resume_ai(resume_text):

    prompt = f"""
    Analyze this resume and return ONLY valid JSON.

    Example:

    {{
      "score": 85,
      "skills": ["Python","Django","SQL"],
      "missing_skills": ["Docker","AWS"],
      "suggestions": "Learn Docker and AWS. Add more projects."
    }}

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    result = response.text

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    data = json.loads(result)

    return data