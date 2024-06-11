import requests
from bs4 import BeautifulSoup
def crawl_and_write(url, html_file):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all movie divs, this needs to be adjusted based on the actual HTML structure of the Metacritic website
    movies = soup.find_all('div', class_='basic_stat product_title')

    movie_items = []
    for movie in movies:
        # Get the movie link and title
        link = movie.find('a').get('href')
        title = movie.find('a').text.strip()

        # If the link and title exist, format them into a <li> tag
        if link and title:
            movie_items.append(f'<li><a href="{link}">{title}</a></li>')

    # Read the content of the html file
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Insert all <li> tags into the <ul> tag
    html = html.replace('<ul style="font-size:16px;margin-left:125px;margin-top:55px;">', '<ul style="font-size:16px;margin-left:125px;margin-top:55px;">\n' + '\n'.join(movie_items))

    # Write the modified HTML content back to the html file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# Crawl and write
crawl_and_write("https://www.metacritic.com/movie", "../templates/America_movies.html")


