import os
import dotenv
import requests
import time
from link_bio.models.live import Live

class Twitch_API:
    
    def __init__(self):
        self.token = None
        self.token_expires = 0
    
    dotenv.load_dotenv()
    
    CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('TWITCH_CLIENT_SECRET')
    
    def generate_token(self):
        response = requests.post(
                                    'https://id.twitch.tv/oauth2/token',
                                    data={
                                            'client_id': self.CLIENT_ID,
                                            'client_secret': self.CLIENT_SECRET,
                                            'grant_type': 'client_credentials'
                                    } 
                    )
        
        if response.status_code == 200:
            data = response.json()
            self.token = data['access_token']
            self.token_expires = time.time()+data['expires_in']
        else: 
            self.token = None
            self.token_expires = 0
    
    def token_valid(self):
        return  time.time() < self.token_expires
    
    def aux_live(self, user_name) -> Live:
        if not self.token_valid():
            self.generate_token()
        
        headers = {
            'Client-ID': self.CLIENT_ID,
            'Authorization': f'Bearer {self.token}'
        }
        
        response = requests.get(
            f'https://api.twitch.tv/helix/streams?user_login={user_name}',
            headers=headers
        )

        if response.status_code == 200 and response.json()['data']:
            data = response.json()['data']
            return Live(live=True, title=data[0]['title'])
        
        return Live(live=False, title="")