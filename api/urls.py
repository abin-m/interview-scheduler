from django.urls import path, include

urlpatterns = [

    path('register/', include('api.registration.urls')),
    path('scheduler/', include('api.scheduler.urls')),
    path('interview/', include('api.interview.urls')),
]
