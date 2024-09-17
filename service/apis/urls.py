from django.urls import path
from .views import get, create

urlpatterns = [
    path('create/', create.CreateService.as_view(),name='create_serivce'),
    path('get/', get.ListServices.as_view(),name='get_user_services'),
]