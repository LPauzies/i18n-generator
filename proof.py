import translators as ts
LIMIT = 4999 # By batch

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

# For all language use ts.google
print(ts.google("Hello", from_language="en", to_language="fr"))