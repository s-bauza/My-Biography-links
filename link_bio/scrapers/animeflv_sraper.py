from bs4 import BeautifulSoup
import requests


class AnimeFlvScraper:

    @staticmethod
    def get_anime_user(name: str, type: str) -> list[dict]:

        anime_already_seen = []
        i = 1
        
        while True:
        
            html_text = requests.get(
                f'https://www3.animeflv.net/perfil/{name}/{type}?page={i}').text

            soup = BeautifulSoup(html_text, 'lxml')

            anime_favorite = soup.find_all('h3', class_='Title')

            anime_favorite_name = [{'title':anime.text} for anime in anime_favorite]

            if not anime_favorite_name:
                break

            anime_already_seen.extend(anime_favorite_name)

            i += 1

        
        return anime_already_seen
