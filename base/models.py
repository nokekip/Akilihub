import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    # avatar
    
    USERNAME_FIELD = 'email'
