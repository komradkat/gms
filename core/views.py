from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/index.html')

def login_view(request):
    return render(request, 'registration/login.html')

def register_view(request):
    return render(request, 'registration/register.html')
