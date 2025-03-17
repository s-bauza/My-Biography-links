import reflex as rx
import link_bio.constants as constants
import io
import csv
from link_bio.api.api import live
from link_bio.models.live import Live
from link_bio.scrapers.animeflv_sraper import AnimeFlvScraper


class PasgeState(rx.State):

    live_status = Live(live=False, title="")

    name: str = ""
    loading: bool = False
    animes: list[dict] = [{}]
    anime_type: str = "favoritos"
    

    async def twitch_live(self):

        self.live_status = await live(constants.TWITCH_USER)

    @rx.event
    def set_name(self, name: str):
        if name and name.strip():
            self.name = name.strip()
        else:
            self.name = ""
            self.animes = [{}]

    @rx.event
    async def get_animes(self):

        if not self.name or self.name.strip() == "":
            return

        self.loading = True
        yield  

        try:
            self.animes = AnimeFlvScraper.get_anime_user(self.name,self.anime_type)
        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.loading = False
            yield  
    
    def _convert_to_csv(self) -> str:
        
        if not self.animes:
            return ""
        
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Title'])
        for anime in self.animes:
            writer.writerow([anime["title"]])
        
        csv_data = output.getvalue()
        output.close()
        return csv_data

    @rx.event
    def download_csv_data(self):
        if not self.animes:
            return rx.window_alert("There are no data to download")
        
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="animes.csv",
        )
    @rx.var
    def has_animes(self) -> bool:
        return self.animes != [{}] 
    
    @rx.var
    def count_animes(self) -> int:
        if self.animes == [{}]:
            return 0
        return len(self.animes)
    
    @rx.event
    async def set_anime_type(self, anime_type: str):
        self.anime_type = anime_type
        if self.name:
           return PasgeState.get_animes()
        
    @rx.event
    def copy_data_table(self):
        texto = "\n".join([anime["title"] for anime in self.animes])
        return rx.set_clipboard(texto)
        
    
    
        