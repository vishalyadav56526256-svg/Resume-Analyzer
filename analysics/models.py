from django.db import models
from django.contrib.auth.models import User
from resumes.models import Resume
    
class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    score = models.IntegerField()
    skills = models.TextField()
    missing_skills = models.TextField()
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.resume.user.username}" 
    
    
       
