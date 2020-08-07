from django.db.utils import OperationalError
from django.shortcuts import get_object_or_404
from .models import Subject, Platform

subject_choices = list()
platform_choices = list()
difficulty_choices = list()
duration_choices = list()

try:
    possible_subjects = Subject.objects.all()
    possible_platforms = Platform.objects.all()

    for subject in possible_subjects:
        subject_choices.append((subject.name, subject.name))
    for platform in possible_platforms:
        platform_choices.append((platform.name, platform.name))

    difficulty_choices = (('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado'))
    duration_choices = (('Curto', 'Curto'), ('Médio', 'Médio'), ('Longo', 'Longo'))
except OperationalError:
    pass