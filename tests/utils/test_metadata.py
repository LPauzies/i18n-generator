import unittest
from i18ngenerator.utils.metadata import AUTHOR, DESCRIPTION, EMAIL, VERSION, NAME

class TestMetadata(unittest.TestCase):

    def test_metadata_is_not_none(self):
        self.assertIsNotNone(VERSION)
        self.assertIsNotNone(EMAIL)
        self.assertIsNotNone(NAME)
        self.assertIsNotNone(DESCRIPTION)
        self.assertIsNotNone(AUTHOR)