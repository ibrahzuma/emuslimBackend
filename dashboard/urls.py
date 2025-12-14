from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='home'),
    path('users/', views.UserManagementView.as_view(), name='users'),
]
