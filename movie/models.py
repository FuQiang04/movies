from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    #actor = models.CharField(max_length=50, default='hello')
