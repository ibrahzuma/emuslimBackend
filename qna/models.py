from django.db import models

class Question(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ANSWERED', 'Answered'),
        ('REJECTED', 'Rejected'),
    )

    question_text = models.TextField(help_text="The user's question.")
    asked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    
    # Answer part
    answer_text = models.TextField(blank=True, null=True, help_text="The Imam's answer.")
    answered_at = models.DateTimeField(blank=True, null=True)
    answered_by = models.CharField(max_length=100, blank=True, help_text="Name of the person attempting to answer")

    def __str__(self):
        return f"{self.question_text[:50]}... ({self.status})"
    
    class Meta:
        ordering = ['-asked_at']
