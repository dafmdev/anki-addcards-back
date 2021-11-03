from typing import Union
import eng_to_ipa as engipa
from manager.utils.clean_ipa import cleaner
from manager.utils.scrapy import scrapy


class CreateIPA:

    def create_ipa_cmu(self, text: str) -> str:

        return cleaner(engipa.convert(text))

    def create_ipa(self, text: str) -> Union[str, None]:
            return self.create_ipa_cmu(text)
