from i18ngenerator.translator import Translator
from i18ngenerator.transformer import Transformer
from i18ngenerator.languages import Language

# Doc : https://github.com/UlionTse/translators

a = "bonjour ! je m'appelle Lucas. et Toi ?"
transformer = Transformer()
print(transformer.capitalize(a))
# print(Translator.batch_translate(text_list=["Bonjour, je suis Lucas", " Accueil", "Salutations"], from_language="fr", to_language="en"))