# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:20:01 2022

@author: Akunuri Arun Deepak 
"""
INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # films app:
    'films.apps.FilmsConfig',
    # add this:
    'django_extensions',
]
    
from films.models import Film, Genre
import csv


def run():
    with open('Medicines.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Film.objects.all().delete()
        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[-1])

            film = Film(title=row[0],
                        year=row[2],
                        genre=genre)
            film.save()    
    