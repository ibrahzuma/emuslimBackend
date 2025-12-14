from django.contrib import admin
from .models import Announcement, DailyReminder

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')

@admin.register(DailyReminder)
class DailyReminderAdmin(admin.ModelAdmin):
    list_display = ('date_for', 'title', 'content_type', 'reference')
    list_filter = ('content_type', 'date_for')
    search_fields = ('title', 'translation', 'reference')
    date_hierarchy = 'date_for'
