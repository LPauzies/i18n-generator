import unittest
from i18ngenerator.languages import Language

from i18ngenerator.transformer import Transformer

transformer = Transformer()

class TestTransformer(unittest.TestCase):

    def test_capitalize(self):
        # Given
        s_fr = "il semblerait que Noé et Irène sont à la plage. ils sont passés par la forêt. c'était hier."
        s_en = "it seems that Noé and Irène are at the beach. they went through the forest. it was yesterday."
        s_es = "parece que Noé e Irène están en la playa. atravesaron el bosque. eso fue ayer."
        s_zh = "Noé 和 Irène 似乎在海滩上。 他们穿过森林。 那是昨天了。"
        s_ru = "кажется, что Ноэ и Ирэн на пляже. они прошли через лес. это было вчера."
        s_ko = "노에와 이렌이 해변에 있는 것 같다. 그들은 숲을 지나갔다. 어제였다."

        # Expected
        s_fr_capitalize = "Il semblerait que Noé et Irène sont à la plage. Ils sont passés par la forêt. C'était hier."
        s_en_capitalize = "It seems that Noé and Irène are at the beach. They went through the forest. It was yesterday."
        s_es_capitalize = "Parece que Noé e Irène están en la playa. Atravesaron el bosque. Eso fue ayer."
        s_zh_capitalize = "Noé 和 Irène 似乎在海滩上。 他们穿过森林。 那是昨天了。"
        s_ru_capitalize = "Кажется, что Ноэ и Ирэн на пляже. Они прошли через лес. Это было вчера."
        s_ko_capitalize = "노에와 이렌이 해변에 있는 것 같다. 그들은 숲을 지나갔다. 어제였다."

        # Do
        self.assertEqual(s_fr_capitalize, transformer.capitalize(s_fr, Language.FRENCH))
        self.assertEqual(s_en_capitalize, transformer.capitalize(s_en, Language.SPANISH))
        self.assertEqual(s_es_capitalize, transformer.capitalize(s_es, Language.SPANISH))
        self.assertEqual(s_zh_capitalize, transformer.capitalize(s_zh, Language.CHINESE))
        self.assertEqual(s_ru_capitalize, transformer.capitalize(s_ru, Language.RUSSIAN))
        self.assertEqual(s_ko_capitalize, transformer.capitalize(s_ko, Language.KOREAN))