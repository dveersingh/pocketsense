from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SettlementViewSet

router = DefaultRouter()
router.register(r'settlements', SettlementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]