from django.db import models

class new_movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    introduction = models.CharField(max_length=500)
    class Meta:
        verbose_name = "new_movies"
        verbose_name_plural= "new_movies"
class recommend_movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    introduction = models.CharField(max_length=500)
    class Meta:
        verbose_name = "recommend_movies"
        verbose_name_plural= "recommend_movies"
class China_movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    introduction = models.CharField(max_length=500)
    class Meta:
        verbose_name = "China_movies"
        verbose_name_plural= "China_movies"
class America_movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    introduction = models.CharField(max_length=500)
    class Meta:
        verbose_name = "America_movies"
        verbose_name_plural= "America_movies"
class Janpa_movies(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    introduction = models.CharField(max_length=500)
    class Meta:
        verbose_name = "Janpa_movies"
        verbose_name_plural= "Janpa_movies"
