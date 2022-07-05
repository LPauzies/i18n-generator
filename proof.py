from i18ngenerator.translator import Translator
from i18ngenerator.languages import Language

# Doc : https://github.com/UlionTse/translators

# To do avant de pratique la traduction
# Parser la chaine de caractère et éliminer les caractères avec accents

# with open("lorem.txt", "r") as fp:
#     l = fp.readlines()
#     l = "".join(l)

# start = 0
# for i in range(0, len(l), LIMIT):
#     res = translators.google(l, from_language="fr", to_language="en")
#     print(res)
#     start+=LIMIT

print(Translator.translate(text="Hello, I am Lucas", from_language=Language.ENGLISH, to_language=Language.FRENCH))
# print(Translator.batch_translate(text_list=["Bonjour, je suis Lucas", " Accueil", "Salutations"], from_language="fr", to_language="en"))