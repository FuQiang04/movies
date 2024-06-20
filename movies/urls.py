
from django.contrib import admin
from django.urls import path
from pygments.lexer import include


from movies import views
urlpatterns = [
    path('', views.index),
    path('china_movies/', views.china_movies),
    path('japan_movies/', views.japan_movies),
    path('America_movies/', views.america_movies),
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
]
