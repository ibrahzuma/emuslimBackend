from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DuaViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'duas', DuaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
