from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.shortcuts import render, redirect
from .serializers import RegisterSerializer


# ---------- API Views ----------

# Signup API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


# Dashboard API (protected)
class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "message": f"Welcome {user.username}, you are authenticated!"
        })


# List all users (protected)
class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.values("id", "username", "email")
        return Response(list(users))


# Logout API (protected, JWT Blacklist)
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"error": "Invalid or expired refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            )


# User Profile API (protected)
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })


# ---------- Template (UI) Views ----------

def home(request):
    return redirect('login_page')


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')
