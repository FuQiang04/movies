import requests
from bs4 import BeautifulSoup
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')
django.setup()
from movie.models import new_movies, recommend_movies, China_movies, America_movies, Janpa_movies

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
]
headers = {
    "User-Agent": random.choice(user_agents)
}
url=[]
url.append("https://www.mgtv.com/lib/3?lastp=list_index&lastp=ch_movie&kind=a1&sort=c2&year=all&edition=182&chargeInfo=a1&fpa=2913&fpos=")
url.append("https://www.mgtv.com/lib/3?lastp=list_index&kind=a1&edition=182&year=all&chargeInfo=a1&sort=c1&area=a1")
url.append("https://www.mgtv.com/lib/3?lastp=list_index&kind=a1&edition=182&year=all&chargeInfo=a1&sort=c2&area=3073")
url.append("https://www.mgtv.com/lib/3?lastp=list_index&kind=a1&edition=182&year=all&chargeInfo=a1&sort=c2&area=other")
url.append("https://www.mgtv.com/lib/3?lastp=list_index&kind=a1&edition=182&year=all&chargeInfo=a1&sort=c2&area=27")
for i in range(5):
    response = requests.get(url[i], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_divs = soup.find_all('div', class_='hitv_vertical scroll-item')
    for movie_div in movie_divs:
        movie_info = movie_div.find('div', class_='hitv_vertical-txtbox')
        href = "https://www.mgtv.com/" + movie_info.a['href']
        title = movie_info.a['title']
        actors = ' '.join([a.get_text() for a in movie_info.find('p', class_='u-desc').find_all('a')])

        screenshot_div = movie_div.find('div', class_='hitv_vertical-screenshot no_size')
        jpg_url = screenshot_div.find('img')['src']
        if i == 0:
            movie = recommend_movies(name=title, href=href, actor=actors, img=jpg_url)
        elif i == 1:
            movie = new_movies(name=title, href=href, actor=actors, img=jpg_url)
        elif i == 2:
            movie = America_movies(name=title, href=href, actor=actors, img=jpg_url)
        elif i == 3:
            movie = Janpa_movies(name=title, href=href, actor=actors, img=jpg_url)
        elif i == 4:
            movie = China_movies(name=title, href=href, actor=actors, img=jpg_url)
        movie.save()
