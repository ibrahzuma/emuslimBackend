from rest_framework import viewsets, permissions
from .models import Announcement, DailyReminder
from .serializers import AnnouncementSerializer, DailyReminderSerializer
from django.utils import timezone

class AnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns active announcements, ordered by newest first.
    """
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.AllowAny]

class DailyReminderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns reminders. Supports filtering by date.
    """
    queryset = DailyReminder.objects.all()
    serializer_class = DailyReminderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date')
        if date:
            return queryset.filter(date_for=date)
        # Default: return all, but typically app requests specific date or 'today'
        return queryset
