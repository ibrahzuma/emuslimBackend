from rest_framework import serializers
from .models import Announcement, DailyReminder

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class DailyReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReminder
        fields = '__all__'
