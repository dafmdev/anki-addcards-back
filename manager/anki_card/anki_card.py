import json
import requests
from manager.utils.file_manager import load_file

class CreateCard:

    def __init__(self):
        self.url = "http://localhost:8765"
        self.data = load_file('manager/assets/base_anki_connet.json', 'json')
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def create_card(self, desk_name: str, front: str, back: str, reading: str):

        self.data['params']['note']['deckName'] = desk_name
        self.data['params']['note']['fields']['Front'] = front.capitalize()
        self.data['params']['note']['fields']['Back'] = back.capitalize()
        self.data['params']['note']['fields']['Reading'] = reading

        r = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)
        return str(r)