from typing import Dict
from manager.IPA.ipa import CreateIPA
from manager.translator.translator import CreateText
from manager.anki_card.anki_card import CreateCard
from manager.polly.polly import CreateSound


class MethodHandler:

    def __init__(self):
        self.create_ipa = CreateIPA()
        self.create_text = CreateText()
        self.create_card = CreateCard()
        self.create_sound = CreateSound()

    def format_response(self, text_en: str, text_es: str, text_ipa: str, url_file_polly: str, status_create_card: str) -> dict:

        response = {}
        if text_en:
            response['english'] = text_en
        if text_es:
            response['spanish'] = text_es
        if text_ipa:
            response['ipa'] = text_ipa
        if url_file_polly:
            response['url_file_polly'] = url_file_polly
        if status_create_card:
            response['create_card'] = status_create_card

        return response


    def detect_modules(self, info: Dict[str, str], recipe: Dict[str, bool]) -> dict:
        create_card = recipe.get('create_card', False)
        text_en: str = ""
        text_es: str = ""
        text_ipa: str = ""
        url_file_polly: str = ""
        name_file_polly: str = ""
        status_create_card: str = ""

        if recipe['translate'] is True:
            text_en, text_es = self.create_text.create_text(info['text'], info['language'])
        if recipe['ipa'] is True:
            text_ipa = self.create_ipa.create_ipa(info['ipa_shape'], text_en)
        if recipe['polly'] is True:
            url_file_polly, name_file_polly = self.create_sound.create_sound(info['text'])
        if create_card is True:
            status_create_card = self.create_card.create_card(info['desk_name'], text_en, text_es, text_ipa, url_file_polly, name_file_polly)

        return self.format_response(text_en, text_es, text_ipa, url_file_polly, status_create_card)

