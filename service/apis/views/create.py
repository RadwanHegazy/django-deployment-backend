from rest_framework.generics import CreateAPIView
from ..serializers import ServiceSerializer
from rest_framework import permissions

class CreateService (CreateAPIView) : 
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }