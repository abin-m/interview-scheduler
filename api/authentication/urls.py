from django.urls import path
from .views import RegisterUser, LoginUser,TokenRefresh

urlpatterns = [
    path('signup/', RegisterUser.as_view(), name='register'),
    path('signin/', LoginUser.as_view(), name='login'),
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
    # ... (other paths)
]