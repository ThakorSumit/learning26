from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    rolechoice=(
        ('admin','admin'),
        ('student','student'),
        ('faculty','faculty')

    )
    role=models.CharField(max_length=10,choices=rolechoice,default='user')
    
