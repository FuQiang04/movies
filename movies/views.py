from django.http import HttpResponse
from django.shortcuts import render

from movie.models import *


def index(request):
    newmovies = new_movies.objects.all()
    recommendmovies = recommend_movies.objects.all()
    context = {'newmovies': newmovies}
    context.update({'recommendmovies': recommendmovies})
    return render(request, 'index.html', context)
def china_movies(request):
    chinamovies = China_movies.objects.all()
    return render(request, 'china_movies.html',{'chinamovies':chinamovies})
def japan_movies(request):
    japanmovies = Janpa_movies.objects.all()
    return render(request, 'japan_movies.html',{'japanmovies':japanmovies})
def america_movies(request):
    Americamovies = America_movies.objects.all()
    return render(request, 'America_movies.html',{'Americamovies':Americamovies})
