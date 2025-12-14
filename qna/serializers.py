from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'asked_at', 'status', 'answer_text', 'answered_at', 'answered_by']
        read_only_fields = ['status', 'answer_text', 'answered_at', 'answered_by']
