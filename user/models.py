from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): #ke thua tu User co san cua Django
    name= models.CharField(max_length=200, blank=False, null=False)
    email= models.EmailField(unique=True)
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['username','email', 'name']
    
    def __str__(self):
        return self.username