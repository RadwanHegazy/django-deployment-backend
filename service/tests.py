from django.test import TestCase
from .models import Service, User
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken

class TestSerivceApp (TestCase) :
    def create_user (self): 
        return User.objects.create_user(
            email='test@gmail.com',
            full_name='test',
            password='123',
        )
    
    def create_service(self):
        service = Service.objects.create(
            user=self.user,
            image='test',
            port=123,
        )
        return service
    
    def setUp(self) -> None:
        self.create_service_endpoint = reverse('create_serivce')
        self.get_service_endpoint = reverse('get_user_services')
        self.user = self.create_user()
        
    
    def test_create_serivce_endpoint (self) : 
        response = self.client.post(self.create_service_endpoint,headers={
            'Authorization' : f"Bearer {AccessToken.for_user(self.user)}"
        }, data={
            'image' : 'image/name'
        })
        
        self.assertEqual(response.status_code, 201)

    def test_create_serivce_endpoint_unauthenticated (self) : 
        response = self.client.post(self.create_service_endpoint, data={
            'image' : 'image/name'
        })
        
        self.assertNotEqual(response.status_code, 201)

    
    def test_get_user_serivces_endpoint (self) : 
        self.create_service()

        response = self.client.get(self.get_service_endpoint,headers={
            'Authorization' : f"Bearer {AccessToken.for_user(self.user)}"
        })

        self.assertEqual(response.status_code, 200)

    def test_get_user_serivces_endpoint_unauthenticated(self): 
        response = self.client.get(self.get_service_endpoint)

        self.assertNotEqual(response.status_code, 200)
