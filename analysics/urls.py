from django.urls import path
from . import views

urlpatterns = [
    path('analyze/<int:resume_id>/', views.analyze_resume, name='analyze_resume'),
]