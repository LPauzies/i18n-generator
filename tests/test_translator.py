import unittest
from i18ngenerator.languages import Language

from i18ngenerator.translator import Translator

class TestTranslator(unittest.TestCase):

    def test_translate_text_from_fr(self):
        # Given
        s_fr = "Il semblerait que Noé et Irène sont à la plage. Ils sont passés par la forêt. C'était hier."

        # Expected
        s_en = "It seems that Noah and Irene are at the beach. They went through the forest. It was yesterday."
        s_es = "Parece que Noé e Irene están en la playa. Pasaron por el bosque. Eso fue ayer."
        s_zh = "看来诺亚和艾琳在海滩上。 他们穿过森林。 那是昨天了。"
        s_ru = "Кажется, что Ной и Ирен на пляже. Они прошли через лес. Это было вчера."
        s_ko = "노아와 아이린이 해변에있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Do
        self.assertEqual(s_en, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.SPANISH))
        self.assertEqual(s_zh, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.CHINESE))
        self.assertEqual(s_ru, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.KOREAN))

    def test_translate_text_from_en(self):
        # Given
        s_en = "It seems that Noah and Irene are at the beach. They went through the forest. It was yesterday."

        # Expected
        s_fr = "Il semble que Noah et Irene soient à la plage. Ils ont traversé la forêt. C'était hier."
        s_es = "Parece que Noé e Irene están en la playa. Pasaron por el bosque. Eso fue ayer."
        s_zh = "看来诺亚和艾琳在海滩上。 他们穿过森林。 那是昨天了。"
        s_ru = "Кажется, что Ной и Ирен на пляже. Они прошли через лес. Это было вчера."
        s_ko = "노아와 아이린이 해변에있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.FRENCH))
        self.assertEqual(s_es, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.SPANISH))
        self.assertEqual(s_zh, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.CHINESE))
        self.assertEqual(s_ru, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.KOREAN))

    def test_translate_text_from_zh(self):
        # Given
        s_zh = "看来诺亚和艾琳在海滩上。 他们穿过森林。 那是昨天了。"

        # Expected
        s_fr = "Il semble que Noah et Irene soient sur la plage. Ils ont traversé la forêt. C'était hier."
        s_es = "Parece que Noé e Irene están en la playa. Pasaron por el bosque. Eso fue ayer."
        s_en = "It seems that Noah and Irene are on the beach. They passed through the forest. That was yesterday."
        s_ru = "Кажется, что Ной и Ирен на пляже. Они прошли через лес. Это было вчера."
        s_ko = "노아와 아이린이 해변에있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.FRENCH))
        self.assertEqual(s_es, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.SPANISH))
        self.assertEqual(s_en, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.ENGLISH))
        self.assertEqual(s_ru, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.KOREAN))

    def test_translate_text_from_es(self):
        # Given
        s_es = "Parece que Noé e Irene están en la playa. Pasaron por el bosque. Eso fue ayer."

        # Expected
        s_fr = "Il semble que Noah et Irene soient sur la plage. Ils ont traversé la forêt. C'était hier."
        s_zh = "看来诺亚和艾琳在海滩上。 他们穿过森林。 那是昨天。"        
        s_en = "It seems that Noah and Irene are on the beach. They passed through the forest. That was yesterday."
        s_ru = "Кажется, что Ной и Ирен на пляже. Они прошли через лес. Это было вчера."
        s_ko = "노아와 아이린이 해변에있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.ENGLISH))
        self.assertEqual(s_ru, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.KOREAN))

    def test_translate_text_from_ru(self):
        # Given
        s_ru = "Кажется, что Ной и Ирен на пляже. Они прошли через лес. Это было вчера."

        # Expected
        s_fr = "Il semble que Noah et Irene sur la plage. Ils ont traversé la forêt. C'était hier."
        s_zh = "似乎诺亚和艾琳在海滩上。 他们穿过森林。 那是昨天了。"        
        s_en = "It seems that Noah and Irene on the beach. They went through the forest. It was yesterday."
        s_es = "Parece que Noé e Irene en la playa. Pasaron por el bosque. Eso fue ayer."        
        s_ko = "해변에서 노아와 아이린이있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.SPANISH))
        self.assertEqual(s_ko, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.KOREAN))

    def test_translate_text_from_ko(self):
        # Given
        s_ko = "해변에서 노아와 아이린이있는 것 같습니다. 그들은 숲을 통과했습니다. 어제였습니다."

        # Expected
        s_fr = "Il semble y avoir Noah et Irene sur la plage. Ils ont traversé la forêt. C'était hier."
        s_zh = "海滩上似乎有诺亚和艾琳。 他们穿过森林。 那是昨天了。"        
        s_en = "There seems to be Noah and Irene on the beach. They passed through the forest. It was yesterday."
        s_es = "Parece que hay Noé e Irene en la playa. Pasaron por el bosque. Eso fue ayer."        
        s_ru = "Кажется, на пляже есть Ной и Ирен. Они прошли через лес. Это было вчера."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.SPANISH))
        self.assertEqual(s_ru, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.RUSSIAN))