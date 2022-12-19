from django.db import models

# Create your models here.
def __str__(self):
    return self.name
class Place(models.Model):
    name=models.CharField(max_length=200)
    imag=models.ImageField(upload_to='pics')
    descrip=models.TextField()

class Person(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
