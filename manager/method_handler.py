from typing import Dict
from manager.IPA.ipa import CreateIPA
from manager.translator.translator import CreateText
from manager.polly.polly import CreateSound


class MethodHandler:

    def __init__(self):
        self.create_ipa = CreateIPA()
        self.create_text = CreateText()
        self.create_sound = CreateSound()

    def format_response(self, text_en: str, text_es: str, text_ipa: str, url_file_polly: str) -> dict:

        response = {}
        if text_en:
            response['en'] = text_en
        if text_es:
            response['es'] = text_es
        if text_ipa:
            response['ipa'] = text_ipa
        if url_file_polly:
            response['url_sound'] = url_file_polly

        return response


    def detect_modules(self, info: Dict[str, str], recipe: Dict[str, bool]) -> dict:
        text_en: str = ""
        text_es: str = ""
        text_ipa: str = ""
        url_file_polly: str = ""
        name_file_polly: str = ""

        if recipe['translate'] is True:
            text_en, text_es = self.create_text.create_text(info['text'], info['language'])
        if recipe['ipa'] is True:
            text_ipa = self.create_ipa.create_ipa(text_en)
        if recipe['polly'] is True:
            url_file_polly, name_file_polly = self.create_sound.create_sound(info['text'])

        return self.format_response(text_en, text_es, text_ipa, url_file_polly)

