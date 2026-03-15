from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/index.html')

def login_view(request):
    return render(request, 'registration/login.html')

def register_view(request):
    return render(request, 'registration/register.html')

def member_list(request):
    return render(request, 'members/list.html')

def member_profile(request, member_id):
    return render(request, 'members/profile.html')

def member_create(request):
    return render(request, 'members/create.html')

def schedule_view(request):
    return render(request, 'classes/schedule.html')
