import link_bio.constants as constants
from link_bio.api.twitch_api import Twitch_API

Twitch_API = Twitch_API()

async def live(user_name) -> bool:
    return Twitch_API.live(user_name)

