import unittest

from myscript import hello


class TestMyScript(unittest.TestCase):
    def test_hello(self):
        actual = hello()
        expected = "hello world!"
        self.assertEqual(actual, expected)

    # def test_goodbye(self):
    #     actual = goodbye()
    #     expected = "goodbye world!"
    #     self.assertEqual(actual, expected)
