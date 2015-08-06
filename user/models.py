from django.db import models
import uuid

class Users(models.Model):
    card = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    birth_date = models.DateField()
    city = models.CharField(max_length = 100)
    email = models.EmailField()
    cellphone = models.CharField(max_length = 10)
    password = models.CharField(max_length = 30)

# Create your models here.

