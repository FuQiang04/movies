from django.contrib import admin
from .models import Movies

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'time']
    search_fields = ['name']