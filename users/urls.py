from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'users', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]