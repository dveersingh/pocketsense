from rest_framework import viewsets
from .models import Settlement
from .serializers import SettlementSerializer

class SettlementViewSet(viewsets.ModelViewSet):
    serializer_class = SettlementSerializer
    queryset = Settlement.objects.all()

    def get_queryset(self):
        return self.queryset.filter(paid_by=self.request.user)