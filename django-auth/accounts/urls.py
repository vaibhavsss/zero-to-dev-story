from django.urls import path
from .views import RegisterView, DashboardAPIView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Auth APIs
    path('signup/', RegisterView.as_view(), name='api_signup'),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Protected APIs
    path('dashboard/', DashboardAPIView.as_view(), name='api_dashboard'),
    path('users/', UserListView.as_view(), name='api_users'),
]
