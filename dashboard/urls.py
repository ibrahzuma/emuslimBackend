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

    # Announcements
    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('announcements/add/', views.AnnouncementCreateView.as_view(), name='announcement_add'),
    path('announcements/<int:pk>/edit/', views.AnnouncementUpdateView.as_view(), name='announcement_edit'),
    path('announcements/<int:pk>/delete/', views.AnnouncementDeleteView.as_view(), name='announcement_delete'),

    # Daily Reminders
    path('reminders/', views.ReminderListView.as_view(), name='reminders'),
    path('reminders/add/', views.ReminderCreateView.as_view(), name='reminder_add'),
    path('reminders/<int:pk>/edit/', views.ReminderUpdateView.as_view(), name='reminder_edit'),
    path('reminders/<int:pk>/delete/', views.ReminderDeleteView.as_view(), name='reminder_delete'),
]
