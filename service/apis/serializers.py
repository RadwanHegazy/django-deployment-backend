from rest_framework import serializers
from ..models import Service

class ServiceSerializer (serializers.ModelSerializer) :
    class Meta:
        model = Service
        exclude = ['user']

    def validate(self, attr) : 
        attr['user'] = self.context.get('user')
        return attr
    