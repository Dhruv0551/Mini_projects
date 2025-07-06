import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"lxml")
movie_titles = soup.find_all(name="h2")


loop_count = 0
for titles in movie_titles[::-1]:
    print(titles.getText())
    with open("movies_list.txt","a") as m_list:
        m_list.write(f"{titles.getText()}\n")
    loop_count += 1
    if loop_count == 100:
        break