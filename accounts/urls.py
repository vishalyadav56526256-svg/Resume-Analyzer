from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
]