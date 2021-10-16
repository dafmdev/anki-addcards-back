from typing import Tuple, Union
from deep_translator import GoogleTranslator

class CreateText:

    def translate_to_es(self, text_en: str) -> str:
        return GoogleTranslator(source="en", target="es").translate(text_en, return_all=True)

    def translate_to_en(self, text_es: str) -> str:
        return GoogleTranslator(source="es", target="en").translate(text_es, return_all=True)

    def create_text(self, text: str, language: str) -> Union[Tuple[str, str], None]:
        if language == 'es':
            text_en = self.translate_to_en(text)
            text_es = text
            return text_en, text_es
        elif language == 'en':
            text_es = self.translate_to_es(text)
            text_en = text
            return text_en, text_es
        else:
            return None
