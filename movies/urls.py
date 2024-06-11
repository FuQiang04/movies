
from django.contrib import admin
from django.urls import path
from movies import views
urlpatterns = [
    path('', views.index),
    path('china_movies/', views.china_movies),
    path('japan_movies/', views.japan_movies),
    path('America_movies/', views.America_movies),
    path('login/',views.login),
path('admin/', admin.site.urls),
]
