from django.contrib import admin
from .models import DonationCampaign

@admin.register(DonationCampaign)
class DonationCampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_amount', 'raised_amount', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
