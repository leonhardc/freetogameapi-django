from django.db import models

# Create your models here.

class Game(models.Model):
    developer = models.CharField(max_length=150, verbose_name='developer')
    profile_url = models.CharField(max_length=150, verbose_name='profile url')
    game_url = models.CharField(max_length=150, verbose_name='game url')
    genre = models.CharField(max_length=20, verbose_name='genre')
    game_id = models.IntegerField(verbose_name='game id')
    platform = models.CharField(max_length=50, verbose_name='platform')
    publisher = models.CharField(max_length=50, verbose_name='publisher')
    release_date = models.DateField(verbose_name='release date')
    short_description = models.CharField(max_length=600, verbose_name='short description')
    thumbnail = models.CharField(max_length=150, verbose_name='thumbnail')
    title = models.CharField(max_length=50, verbose_name='title')


