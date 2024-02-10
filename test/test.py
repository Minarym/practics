import unittest
from src.main import sum


class MainTest(unittest.TestCase):

    def test_sum(self):
        a, b = 1, 2
        self.assertEqual(a + b, sum(a, b))
