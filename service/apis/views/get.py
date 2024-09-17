from rest_framework.generics import ListAPIView
from ..serializers import ServiceSerializer, Service
from rest_framework import permissions

class ListServices (ListAPIView) :
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
