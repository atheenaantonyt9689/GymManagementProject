from django.db import models


# Create your models here.

class FitHubMember(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    designation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
