from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=31, unique=True)

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
    link = models.URLField(default='http://127.0.0.1:8000/', max_length=200)

    def __str__(self):
        return self.name


class Search(models.Model):
    subject = models.CharField(max_length=31)
    platform = models.CharField(max_length=31)
    difficulty = models.CharField(max_length=31)
    duration = models.CharField(max_length=31)
    language = models.CharField(default='default', max_length=31)