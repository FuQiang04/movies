from django.contrib import admin
from movie.models import *


@admin.register(Janpa_movies)
class Janpa_moviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'href', 'actor', 'img']
    search_fields = ['name']
    list_display_links = ['name']
@admin.register(China_movies)
class China_moviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'href', 'actor', 'img']
    search_fields = ['name']
    list_display_links = ['name']
@admin.register(America_movies)
class America_moviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'href', 'actor', 'img']
    search_fields = ['name']
    list_display_links = ['name']
@admin.register(recommend_movies)
class recommend_moviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'href', 'actor', 'img']
    search_fields = ['name']
    list_display_links = ['name']
@admin.register(new_movies)
class new_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name','href','actor','img']
    search_fields = ['name']
    list_display_links = ['name']