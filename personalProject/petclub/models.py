from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField()
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    
    class Meta:
        managed = True


