from django.contrib import admin
from django.urls import path
from core.views import dashboard, login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
