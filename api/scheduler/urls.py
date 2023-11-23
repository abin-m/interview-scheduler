from django.urls import path
from . import views  # Replace 'your_app_name' with the actual name of your Django app

urlpatterns = [
    path('find-slots/<int:candidate_id>/<int:interviewer_id>/', views.schedule_interview, name='schedule-interview'),
]