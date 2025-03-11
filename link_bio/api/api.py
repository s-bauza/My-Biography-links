from link_bio.api.twitch_api import Twitch_API
from link_bio.models.live import Live

Twitch_API = Twitch_API()

async def live(user_name) -> Live:
    return Twitch_API.aux_live(user_name)

