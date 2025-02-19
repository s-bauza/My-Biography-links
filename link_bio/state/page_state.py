import reflex as rx
import link_bio.constants as constants
from link_bio.api.api import live


class PasgeState(rx.State):
    is_alive: bool  
    
    async def twitch_live(self) -> bool:
        
        self.is_alive = await live(constants.TWITCH_USER)
        