import unittest
import io
import contextlib

from i18ngenerator.utils.utils import timeit

class TestUtils(unittest.TestCase):

    def test_timeit(self):
        # Given
        x = 2

        @timeit
        def dummy_function(x: int) -> int:
            return x**2

        # Expected
        expected_in = "Done in"

        # Do
        with io.StringIO() as buffer_stdout:
            with contextlib.redirect_stdout(buffer_stdout):
                dummy_function(x)
            self.assertIn(expected_in, buffer_stdout.getvalue())
        


    