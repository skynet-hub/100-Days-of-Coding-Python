from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web = response.text

soup = BeautifulSoup(movies_web, 'html.parser')
movies = soup.findAll(name="h3", class_="title")

final_movies = [movie.getText() for movie in movies][::-1]

with open('movies.csv', mode='w') as f:
    for movie in final_movies:
        f.write(movie + '\n')
        