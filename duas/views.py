from rest_framework import viewsets, permissions
from .models import Category, Dua
from .serializers import CategorySerializer, DuaSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] # Publicly viewable (controlled by API Key middleware)

class DuaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dua.objects.all()
    serializer_class = DuaSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['category']
