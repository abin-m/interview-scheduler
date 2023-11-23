from django.urls import path
from . import views

urlpatterns = [
    path('candidate/', views.candidate_availability, name='candidate-availability'),
    path('interviewer/', views.interviewer_availability, name='interviewer-availability'),
]
