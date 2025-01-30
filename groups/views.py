from rest_framework import viewsets
from .models import Group
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user)