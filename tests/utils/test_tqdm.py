import unittest

from i18ngenerator.utils.tqdm import infinite_generator

class TestTQDM(unittest.TestCase):

    def test_infinite_generator(self):
        generator = infinite_generator()
        self.assertIsNone(next(generator))