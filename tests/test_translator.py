import unittest
from i18ngenerator.languages import Language

from i18ngenerator.translator import Translator

class TestTranslator(unittest.TestCase):

    def test_translate_text_from_fr(self):
        # Given
        s_fr = "Je suis à la plage. Demain, j'irai chez le docteur. Hier, j'étais à l'école."

        # Expected
        s_en = "I am at the beach. Tomorrow I will go to the doctor. Yesterday I was in school."
        s_es = "Estoy en la playa. Mañana iré al médico. Ayer estaba en la escuela."
        s_zh = "我在海滩。 明天，我将去看医生。 昨天我在学校。"
        s_ru = "Я на пляже. Завтра я пойду к врачу. Вчера я учился в школе."
        s_ko = "나는 해변에있다. 내일, 나는 의사에게 갈 것이다. 어제 나는 학교에 있었다."

        # Do
        self.assertEqual(s_en, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.SPANISH))
        self.assertEqual(s_zh, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.CHINESE))
        self.assertEqual(s_ru, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language=Language.KOREAN))

    def test_translate_text_from_en(self):
        # Given
        s_en = "I am at the beach. Tomorrow I will go to the doctor. Yesterday I was in school."

        # Expected
        s_fr = "Je suis à la plage. Demain, j’irai chez le médecin. Hier, j’étais à l’école."
        s_es = "Estoy en la playa. Mañana iré al médico. Ayer estaba en la escuela."
        s_zh = "我在海滩。 明天我将去看医生。 昨天我在学校。"
        s_ru = "Я на пляже. Завтра пойду к врачу. Вчера я учился в школе."
        s_ko = "나는 해변에있다. 내일 나는 의사에게 갈 것이다. 어제 나는 학교에 있었다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.FRENCH))
        self.assertEqual(s_es, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.SPANISH))
        self.assertEqual(s_zh, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.CHINESE))
        self.assertEqual(s_ru, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_en, from_language=Language.ENGLISH, to_language=Language.KOREAN))

    def test_translate_text_from_zh(self):
        # Given
        s_zh = "我在海滩。 明天我将去看医生。 昨天我在学校。"

        # Expected
        s_fr = "Je suis sur la plage. J'irai chez un médecin demain. J'étais à l'école hier."
        s_es = "Estoy en la playa. Mañana iré a un médico. Ayer estuve en la escuela."
        s_en = "I'm on the beach. I will go to a doctor tomorrow. I was at school yesterday."
        s_ru = "Я на пляже. Завтра пойду к врачу. Я был в школе вчера."
        s_ko = "나는 해변에있다. 내일 의사에게 갈 게요. 나는 어제 학교에 있었다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.FRENCH))
        self.assertEqual(s_es, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.SPANISH))
        self.assertEqual(s_en, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.ENGLISH))
        self.assertEqual(s_ru, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_zh, from_language=Language.CHINESE, to_language=Language.KOREAN))

    def test_translate_text_from_es(self):
        # Given
        s_es = "Estoy en la playa. Mañana iré al médico. Ayer estaba en la escuela."

        # Expected
        s_fr = "Je suis sur la plage. Demain, j’irai chez le médecin. Hier, j’étais à l’école."
        s_zh = "我在海滩。 明天我要去医生办公室。 昨天我在学校。"
        s_en = "I'm on the beach. Tomorrow I will go to the doctor. Yesterday I was at school."
        s_ru = "Я на пляже. Завтра я пойду в кабинет врача. Вчера я учился в школе."
        s_ko = "나는 해변에있다. 내일 나는 의사의 사무실에 간다. 어제 나는 학교에 있었다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.ENGLISH))
        self.assertEqual(s_ru, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.RUSSIAN))
        self.assertEqual(s_ko, Translator.translate_text(s_es, from_language=Language.SPANISH, to_language=Language.KOREAN))

    def test_translate_text_from_ru(self):
        # Given
        s_ru = "Я на пляже. Завтра пойду к врачу. Вчера я был в школе."

        # Expected
        s_fr = "Je suis sur la plage. Je vais aller chez le médecin demain. Hier, j'étais à l'école."
        s_zh = "我在海滩上。 我明天去看医生。 昨天我在学校。"
        s_en = "I'm on the beach. I’ll go to the doctor tomorrow. Yesterday I was at school."
        s_es = "Estoy en la playa. Iré al médico mañana. Ayer estaba en la escuela."
        s_ko = "나는 해변에있다. 내일 의사에게 갈 게요. 어제 나는 학교에 있었다."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.SPANISH))
        self.assertEqual(s_ko, Translator.translate_text(s_ru, from_language=Language.RUSSIAN, to_language=Language.KOREAN))

    def test_translate_text_from_ko(self):
        # Given
        s_ko = "나는 해변에있다. 내일 나는 의사에게 갈 것이다. 어제 나는 학교에 있었다."

        # Expected
        s_fr = "Je suis sur la plage. Demain, j'irai chez le médecin. Hier, j'étais à l'école."
        s_zh = "我在海滩上。 明天我将去看医生。 昨天我在学校。"
        s_en = "I am on the beach. Tomorrow I will go to the doctor. Yesterday I was at school."
        s_es = "Estoy en la playa. Mañana iré al médico. Ayer estaba en la escuela."
        s_ru = "Я на пляже. Завтра пойду к врачу. Вчера я учился в школе."

        # Do
        self.assertEqual(s_fr, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.FRENCH))
        self.assertEqual(s_zh, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.CHINESE))
        self.assertEqual(s_en, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.ENGLISH))
        self.assertEqual(s_es, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.SPANISH))
        self.assertEqual(s_ru, Translator.translate_text(s_ko, from_language=Language.KOREAN, to_language=Language.RUSSIAN))

    def test_translate_text_from_el(self):
        # Given
        s_el = "Είμαι στην παραλία. Αύριο θα πάω στο γιατρό. Χθες ήμουν στο σχολείο."

        # Expected
        s_az = "Çimərdəyəm. Sabah həkimə gedəcəm. Dünən məktəbdə idim."

        # Do
        self.assertEqual(s_az, Translator.translate_text(s_el, from_language=Language.GREEK, to_language=Language.AZERBAIJANI))

    def test_translate_text_not_instance_of_language_from(self):
        # Given
        s_fr = "Il semble y avoir Noah et Irene sur la plage. Ils ont traversé la forêt. C'était hier."

        with self.assertRaises(TypeError):
            Translator.translate_text(s_fr, from_language="fr", to_language=Language.SPANISH)

    def test_translate_text_not_instance_of_language_to(self):
        # Given
        s_fr = "Il semble y avoir Noah et Irene sur la plage. Ils ont traversé la forêt. C'était hier."

        with self.assertRaises(TypeError):
            Translator.translate_text(s_fr, from_language=Language.FRENCH, to_language="es")

    def test_translate_text_not_instance_of_language_from_to(self):
        # Given
        s_fr = "Il semble y avoir Noah et Irene sur la plage. Ils ont traversé la forêt. C'était hier."

        with self.assertRaises(TypeError):
            Translator.translate_text(s_fr, from_language="fr", to_language="es")