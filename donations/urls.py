from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationCampaignViewSet

router = DefaultRouter()
router.register(r'campaigns', DonationCampaignViewSet, basename='campaign')

urlpatterns = [
    path('', include(router.urls)),
]
