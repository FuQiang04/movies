from django.contrib import admin
from movie.models import *

@admin.register(new_movies)
class new_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time','href','director','introduction']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['time']
@admin.register(Janpa_movies)
class Janpa_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time','href','director','introduction']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['time']
@admin.register(China_movies)
class China_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time','href','director','introduction']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['time']
@admin.register(America_movies)
class America_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time','href','director','introduction']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['time']
@admin.register(recommend_movies)
class recommend_moviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time','href','director','introduction']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['time']