from translate import Translator

def translate_to_languages(phrase, target_languages):
    translations = {}

    for lang in target_languages:
        translator = Translator(to_lang=lang)
        translation = translator.translate(phrase)
        translations[lang] = translation

    return translations

# List of target languages (ISO 639-1 language codes)
target_languages = ["en", "es", "fr", "de", "ar", "zh", "ru"]

phrase = "good morning"

translations = translate_to_languages(phrase, target_languages)

for lang, translation in translations.items():
    print(f"{lang}: {translation}")
