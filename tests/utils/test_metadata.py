import unittest
from i18ngenerator.utils.metadata import VERSION

class TestMetadata(unittest.TestCase):

    def test_version_is_not_none(self):
        self.assertIsNotNone(VERSION)