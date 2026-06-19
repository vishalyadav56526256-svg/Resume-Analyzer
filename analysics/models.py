# from django.db import models
# from django.contrib.auth.models import User

# class Resume(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='resumes/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
# class ResumeAnalysis(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     score = models.IntegerField()
#     extracted_skills = models.TextField()
#     missing_skills = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Analysis for {self.resume.name}" 
    
    
       
