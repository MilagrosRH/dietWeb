from django.db import models

# Create your models here.

class Food():
    kcal=models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Symptom():
    name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name