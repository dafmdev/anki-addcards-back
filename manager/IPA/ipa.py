from typing import Union
import eng_to_ipa as engipa
from manager.utils.clean_ipa import cleaner
from manager.utils.scrapy import scrapy


class CreateIPA:

    def create_ipa_cmu(self, text: str) -> str:

        return cleaner(engipa.convert(text))

    def create_ipa_lexico(self, text: str) -> str:
        url = "https://www.lexico.com/en/definition/"
        selector = "span.phoneticspelling"
        titles = scrapy(url, selector, text)

        if titles:
            text_ipa = titles[1].text
            text_ipa = cleaner(text_ipa)

            if not text_ipa:
                text_ipa = titles[0].text
                text_ipa = cleaner(text_ipa)
                return text_ipa
            return text_ipa
        else:
            return None

    def create_ipa(self, shape: str, text: str) -> Union[str, None]:
        if shape == 'cmu':
            return self.create_ipa_cmu(text)
        elif shape == 'lexico':
            return self.create_ipa_lexico(text)
        else:
            return None
