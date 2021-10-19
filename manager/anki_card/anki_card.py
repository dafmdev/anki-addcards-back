import json
import time
import requests
from manager.utils.file_manager import load_file

class CreateCard:

    def __init__(self):
        self.url = "http://localhost:8765"
        self.data = load_file('manager/assets/base_anki_connet.json', 'json')
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def create_card(self, desk_name: str, front: str, back: str, reading: str, url_file_polly: str, name_file_polly: str):

        self.data['params']['note']['deckName'] = desk_name
        self.data['params']['note']['fields']['Front'] = front.capitalize()
        self.data['params']['note']['fields']['Back'] = back.capitalize()
        self.data['params']['note']['fields']['Reading'] = reading
        self.data['params']['note']['audio'][0]['url'] = url_file_polly
        self.data['params']['note']['audio'][0]['filename'] = name_file_polly.lower()

        time.sleep(20)

        r = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)
        return str(r)