from unittest import TestCase
import string
import random

from kata import alphabet_position


def ap(text):
    text = text.lower().strip()
    return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in string.ascii_letters])


class Test(TestCase):
    def test_alphabet_position_fixed(self):
        # Tests for each letter
        for letter in string.ascii_lowercase:
            self.assertEqual(alphabet_position(letter), ap(letter))

        # Tests for non-letters:
        self.assertEqual(alphabet_position("-.-'"), "")

    def test_alphabet_position_random(self):

        for i in range(100):
            x = ''.join(random.choice(string.ascii_letters) for _ in range(100))
            self.assertEqual(alphabet_position(x), ap(x))
