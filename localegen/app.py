import time
from enum import Enum

import yaml
from deep_translator import GoogleTranslator as Translator


class ValidLanguage(Enum):
    SPANISH = 'es',
    DUTCH = 'nl',
    GERMAN = 'de',
    FRENCH = 'fr',
    ITALIAN = 'it',
    PORTUGUESE = 'pt',
    RUSSIAN = 'ru',
    JAPANESE = 'ja',
    KOREAN = 'ko',
    CHINESE = 'zh-CN',

    @staticmethod
    def from_str(string: str):
        match string:
            case 'es':
                return ValidLanguage.SPANISH
            case 'nl':
                return ValidLanguage.DUTCH
            case 'de':
                return ValidLanguage.GERMAN
            case 'fr':
                return ValidLanguage.FRENCH
            case 'it':
                return ValidLanguage.ITALIAN
            case 'pt':
                return ValidLanguage.PORTUGUESE
            case 'ru':
                return ValidLanguage.RUSSIAN
            case 'ja':
                return ValidLanguage.JAPANESE
            case 'ko':
                return ValidLanguage.KOREAN
            case 'zh':
                return ValidLanguage.CHINESE
            case _:
                raise ValueError(f'Invalid language: {string}')


class LocaleGenerator:
    def __init__(self, english_yml: str) -> None:
        with open(english_yml, 'r', encoding='utf8') as stream:
            try:
                self.locale_mappings = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def generate_locale(self, language: ValidLanguage) -> None:
        time1 = time.time()

        try:
            translator = Translator(source='en', target=language.value[0])
            texts = list(self.locale_mappings.values())
            translations = translator.translate_batch(texts)
        except Exception as e:
            raise e

        with open(f'locales/messages.{language.value[0]}.yml', 'w', encoding='utf8') as outfile:
            for (key, value) in zip(self.locale_mappings.keys(), translations):
                real_val = value.replace('\n', '\\n')
                outfile.write(f'{key}: "{real_val}"\n')

        time2 = time.time()
        print(f'Translated {len(translations)} sentences in {time2 - time1} seconds.')
