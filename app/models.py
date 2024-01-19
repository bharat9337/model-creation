from django.db import models

# Create your models here.
from app.models import *



class State(models.Model):
    Sno=models.BigIntegerField(primary_key=True)   
    State_name=models.CharField(max_length=100)
    Capital=models.CharField(max_length=100)

    def __str__(self):
        return self.State_name

class Capital(models.Model):
    Sname=models.ForeignKey(State,on_delete=models.CASCADE)
    Cno=models.BigIntegerField(primary_key=True)
    Capital_name=models.CharField(max_length=100)
    Population=models.BigIntegerField()

    def __str__(self):
       return self.Capital_name


