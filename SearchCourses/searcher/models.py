from django.db import models
from django.contrib.auth.models import User
import datetime

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


class Difficulty(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name

class Duration(models.Model):   # Classification, not duration in time unities
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=31)
    subject = models.CharField(default='default', max_length=31)
    platform = models.CharField(default='default', max_length=31)
    difficulty = models.CharField(default='default', max_length=31)
    language = models.CharField(default='default', max_length=31)
    duration = models.CharField(default='default', max_length=31)
    duration_time = models.TimeField(default=datetime.time(16,00))
    description = models.TextField(max_length=2047)
    evaluation = models.FloatField(default=0.0)
    link = models.URLField(default='http://127.0.0.1:8000/', max_length=200)

    def __str__(self):
        return self.name


class Search(models.Model):
    subject = models.CharField(max_length=31)
    platform = models.CharField(max_length=31)
    difficulty = models.CharField(max_length=31)
    duration = models.CharField(max_length=31)
    language = models.CharField(default='default', max_length=31)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='searchs')
    created_at = models.DateTimeField(auto_now_add=True)
