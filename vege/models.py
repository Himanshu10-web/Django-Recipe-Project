from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recepie(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank= True) #this gives all the field by default like username password first_name last name etc
    receipe_name = models.CharField(max_length = 100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to = "receipe")