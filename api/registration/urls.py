from django.urls import path,include
from . import views

urlpatterns = [
    path('candidates/', views.candidate_list, name='candidate-list'),
    path('candidate/<int:pk>/', views.candidate_details, name='candidate-details'),
    path('interviewers/', views.interviewer_list, name='interviewer-list'),
    path('interviewer/<int:pk>/', views.interviewer_details, name='interviewer-details'),

    path('availability/', include('api.registration.availability_pro.urls')),
]
