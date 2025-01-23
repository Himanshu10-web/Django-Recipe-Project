from django.db import models

# Create your models here.

#CRUD
#Create - using .create() method and for dict using create(**dict_name)

class Student(models.Model):
    # int = models.AutoField()    default field created by django automatically 
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    

class Cars(models.Model):
    car_name = models.CharField(max_length = 500)
    top_speed = models.IntegerField(default = 50)
    model_year = models.IntegerField()

    def __str__(self) -> str:
        return self.car_name