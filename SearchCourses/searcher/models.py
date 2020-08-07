from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=31, unique=True)
    evaluation = models.FloatField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=31)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='courses')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    last_updated = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(max_length=31)
    duration = models.TimeField()
    duration_evaluation = models.CharField(max_length=15)
    description = models.TextField(max_length=2047)
    evaluation = models.FloatField()

    def __str__(self):
        return self.name


class Search(models.Model):
    subject = models.CharField(max_length=31)
    platform = models.CharField(max_length=127)
    difficulty = models.CharField(max_length=63)
    duration = models.CharField(max_length=31)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='searchs')
    created_at = models.DateTimeField(auto_now_add=True)
