from django.shortcuts import render, redirect
from .models import Resume

def upload_resume(request):
    if request.method == 'POST': 
        resume_file = request.FILES.get('resume_file')
        
        Resume.objects.create(
                user=request.user,
                resume_file=resume_file
            )
        return redirect('upload_resume')
    return render(request, 'resumes/upload.html')