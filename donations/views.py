from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import DonationCampaign
from .serializers import DonationCampaignSerializer

class DonationCampaignViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API for listing donation campaigns.
    """
    queryset = DonationCampaign.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = DonationCampaignSerializer
    permission_classes = [AllowAny]
