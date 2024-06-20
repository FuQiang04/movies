from django.http import HttpResponse
from django.shortcuts import render

from movie.models import *
from movie.forms import SearchForm

def index(request):
    newmovies = new_movies.objects.all()
    recommendmovies = recommend_movies.objects.all()
    form = SearchForm()
    context = {'newmovies': newmovies, 'recommendmovies': recommendmovies, 'form': form}
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
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            results = new_movies.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = SearchForm()
    #return render(request, 'index.html', {'form': form})
    