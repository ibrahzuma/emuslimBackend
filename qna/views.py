from rest_framework import viewsets, permissions, mixins
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    API for submitting questions and reading answered ones.
    - POST: Submit a question (status PENDING).
    - GET: List/Retrieve active questions (mostly ANSWERED ones, or user's own if auth implemented).
           For now, public GET lists only ANSWERED/PUBLISHED questions.
    """
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Only show answered questions to the public
        return Question.objects.filter(status='ANSWERED')
