from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    pawd = models.CharField(max_length=128)

class Person(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)