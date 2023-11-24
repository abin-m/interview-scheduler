from django.urls import path
from . import views

urlpatterns = [
    path('candidate/', views.candidate_availability, name='candidate-availability'),
    path('interviewer/', views.interviewer_availability, name='interviewer-availability'),
    path('candidate/delete/<int:interview_code>/', views.delete_candidate_availability, name='delete-candidate-availability'),
    path('interviewer/delete/<int:interview_code>/', views.delete_interviewer_availability, name='delete-interviewer-availability'),
]