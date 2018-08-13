from django.db import models

# Create your models here.

class UName(models.Model):
    name= models.CharField(max_length=20)
    age = models.IntegerField(max_length=10)
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return self.name