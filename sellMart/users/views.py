from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


# views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('user-list')  # Or wherever you want to redirect after signup
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user-signin')  # Redirect to the sign-in page after signup
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('user-list')  # Redirect after successful login
#     else:
#         form = AuthenticationForm()

#     return render(request, 'signin.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product-list')  # Redirect to Product List page
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})
