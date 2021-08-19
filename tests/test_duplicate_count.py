from random import randint, choice
from string import ascii_letters, digits
from unittest import TestCase

from kata import duplicate_count


class Test(TestCase):
    def test_duplicate_count_basic(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)

    def test_duplicate_count_random(self):
        def sol(s):
            s = s.lower()
            return len(set(s)) - len(s) + sum([s.count(c) for c in set(s) if s.count(c) > 1])

        for _ in range(100):
            strng = ''.join(choice(ascii_letters + digits) for i in range(0, randint(0, 100)))

            # Testing for duplicate_count
            self.assertEqual(duplicate_count(strng), sol(strng))
