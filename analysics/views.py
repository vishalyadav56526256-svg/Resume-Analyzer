# from django.shortcuts import render
# from resumes.models import Resume
# from .models import ResumeAnalysis

# from .utils import (
#     extract_text,
#     find_skills,
#     calculate_score,
#     get_missing_skills
# )

# def analyze_resume(request, resume_id):

#     resume = Resume.objects.get(
#         id=resume_id
#     )

#     text = extract_text(
#         resume.resume_file.path
#     )

#     skills = find_skills(text)

#     score = calculate_score(skills)

#     missing = get_missing_skills(skills)

#     analysis = ResumeAnalysis.objects.create(
#         user=request.user,
#         resume=resume,
#         score=score,
#         skills=", ".join(skills),
#         missing_skills=", ".join(missing),
#         suggestions="Improve missing skills"
#     )

#     return render(
#         request,
#         "analysics/results.html",
#         {"analysis": analysis}
#     )

from django.shortcuts import redirect, render
from resumes.models import Resume
from .models import ResumeAnalysis

from .utils import (
    extract_text,
    analyze_resume_ai
)


def analyze_resume(request, resume_id):

    resume = Resume.objects.get(
        id=resume_id
    )

    text = extract_text(
        resume.resume_file.path
    )

    ai_data = analyze_resume_ai(text)

    analysis = ResumeAnalysis.objects.create(
        user=request.user,
        resume=resume,

        score=ai_data["score"],

        skills=", ".join(
            ai_data["skills"]
        ),

        missing_skills=", ".join(
            ai_data["missing_skills"]
        ),

        suggestions=ai_data["suggestions"]
    )
    

    return render(
        request,
        "analysics/results.html",
        {
            "analysis": analysis
        }
    )

