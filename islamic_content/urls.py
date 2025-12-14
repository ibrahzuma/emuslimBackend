from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, DailyReminderViewSet

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'reminders', DailyReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
