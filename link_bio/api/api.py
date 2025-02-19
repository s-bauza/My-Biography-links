import link_bio.constants as constants
from link_bio.api.twitch_api import Twitch_API

Twitch_API = Twitch_API()

async def live(user_name) -> dict:
    return Twitch_API.aux_live(user_name)

