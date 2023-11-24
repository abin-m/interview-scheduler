from django.contrib import admin
from .models import CandidateAvailability,InterviewerAvailability
# Register your models here.
admin.site.register(CandidateAvailability)
admin.site.register(InterviewerAvailability)