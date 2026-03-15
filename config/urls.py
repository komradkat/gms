from django.contrib import admin
from django.urls import path
from core.views import (
    dashboard, login_view, register_view, 
    member_list, member_profile, member_create,
    schedule_view, trainer_list, trainer_profile,
    staff_list
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('members/', member_list, name='member_list'),
    path('members/add/', member_create, name='member_create'),
    path('members/<int:member_id>/', member_profile, name='member_profile'),
    path('schedule/', schedule_view, name='schedule'),
    path('trainers/', trainer_list, name='trainer_list'),
    path('trainers/<int:trainer_id>/', trainer_profile, name='trainer_profile'),
    path('staff/', staff_list, name='staff_list'),
]
