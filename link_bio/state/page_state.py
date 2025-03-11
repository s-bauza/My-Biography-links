import reflex as rx
import link_bio.constants as constants
from link_bio.api.api import live
from link_bio.models.live import Live


class PasgeState(rx.State):
    
    live_status = Live(live=False,title="") 
    
    async def twitch_live(self):
        
       self.live_status = await live(constants.TWITCH_USER)
       
        