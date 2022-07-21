from email import message
from django.db import models


# Create your models here.
class Infor(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name},{self.email},{self.message}"

