from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='home'),
    path('users/', views.UserManagementView.as_view(), name='users'),
    
    # Duas
    path('duas/', views.DuaListView.as_view(), name='duas'),
    path('duas/add/', views.DuaCreateView.as_view(), name='dua_add'),
    path('duas/<int:pk>/edit/', views.DuaUpdateView.as_view(), name='dua_edit'),
    path('duas/<int:pk>/delete/', views.DuaDeleteView.as_view(), name='dua_delete'),

    # Categories
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
