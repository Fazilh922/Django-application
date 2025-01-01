from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Country(models.Model):
    continent = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.country

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.created_by.username}"


class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name