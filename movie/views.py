from django.shortcuts import render

def china_movies(request):
    return render(request, 'china_movies.html')
def japan_movies(request):
    return render(request, 'japan_movies.html')
def America_movies(request):
    return render(request, 'America_movies.html')
def login(request):
    return render(request, 'login.html')
