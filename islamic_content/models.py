from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=True, help_text="If unchecked, this won't show in the app.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class DailyReminder(models.Model):
    CONTENT_TYPES = (
        ('VERSE', 'Quran Verse'),
        ('HADITH', 'Hadith'),
        ('QUOTE', 'Islamic Quote'),
    )

    date_for = models.DateField(unique=True, help_text="Date this content should be displayed.")
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES, default='VERSE')
    title = models.CharField(max_length=200, help_text="e.g., 'Verse of the Day'")
    arabic_text = models.TextField(blank=True, null=True)
    translation = models.TextField(help_text="English translation or main content.")
    reference = models.CharField(max_length=100, blank=True, help_text="e.g., 'Sahih Bukhari 1:1' or 'Surah Al-Fatiha'")

    def __str__(self):
        return f"{self.date_for} - {self.title}"

    class Meta:
        ordering = ['-date_for']
