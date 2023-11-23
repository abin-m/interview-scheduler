from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.interview_list, name='interview-list'),
    path('<str:interview_code>/', views.interview_detail, name='interview-detail'),
]