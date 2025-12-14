from django.db import models

class DonationCampaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, help_text="Goal amount (e.g., 5000.00)")
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, help_text="Amount collected so far")
    bank_details = models.TextField(help_text="Instructions for payment (Bank Name, Account No, etc.)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def progress_percentage(self):
        if self.target_amount > 0:
            return int((self.raised_amount / self.target_amount) * 100)
        return 0
