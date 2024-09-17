from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServicePanel (admin.ModelAdmin) : 
    list_display = ['image','user','port','is_online']