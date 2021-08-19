import random
import string
from codecs import encode
from unittest import TestCase

from kata import rot13


def sol(s):
    return encode(s, 'rot13')


class Test(TestCase):
    def static(self, d):
        self.assertEqual(rot13(d), sol(d))
        self.assertEqual(rot13(rot13(d)), d)

    def test_rot13_fixed(self):
        # rot13 on predefined strings
        self.static("test")
        self.static("test")
        self.static("Test")
        self.static("Codewars")
        self.static("Avoid success at all costs!")
        self.static("10+2 is twelve.")
        self.static("abcdefghijklmnopqrstuvwxyz")

    def test_rot13_random(self):
        # rot13 on random strings
        for _ in range(100):
            word = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + " " + string.digits)
                           for _ in range(16))
            self.static(word)
