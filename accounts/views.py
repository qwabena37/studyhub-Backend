from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .Serializers import RegisterSerializer

# --- DRF API View for User Registration ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Allow anyone to register


# --- Django views for session-based login/logout/register pages ---

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your homepage or dashboard
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'accounts/login.html', context)

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        context = {}

        if password != password_confirm:
            context['error'] = "Passwords do not match."
            return render(request, 'accounts/register.html', context)

        if User.objects.filter(username=username).exists():
            context['error'] = "Username already taken."
            return render(request, 'accounts/register.html', context)

        # Create the new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('accounts:login')

    return render(request, 'accounts/register.html')
