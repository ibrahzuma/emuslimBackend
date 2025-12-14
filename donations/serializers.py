from rest_framework import serializers
from .models import DonationCampaign

class DonationCampaignSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.IntegerField(read_only=True)

    class Meta:
        model = DonationCampaign
        fields = '__all__'
