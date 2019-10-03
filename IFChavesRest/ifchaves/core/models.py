from django.db import models
from django.core.validators import MaxLengthValidator

class Admin(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.usuario
    
class User(models.Model):
    name = models.CharField(max_length=50)
    registry = models.IntegerField(validators=[MaxLengthValidator(14)])
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Key(models.Model):
    keyNumber = models.IntegerField()
    block = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)
    status = models.BooleanField()

    def __str__(self):
        return self.keyNumber

class Lending(models.Model):
    keyId = models.IntegerField()
    userId = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()    
    status = models.BooleanField()

    def __str__(self):
        return self.keyId
    

    