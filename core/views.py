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

def trainer_list(request):
    return render(request, 'trainers/list.html')

def trainer_profile(request, trainer_id):
    return render(request, 'trainers/profile.html')

def staff_list(request):
    return render(request, 'trainers/staff_list.html')
