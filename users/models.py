from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Objects (BaseUserManager) : 
    
    def create_user(self, password, **fields) : 
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **fields) : 
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(**fields)


class User (AbstractUser) : 
    first_name = None
    last_name = None
    username = None
    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = Objects()

    def __str__(self) -> str:
        return self.full_name
    
