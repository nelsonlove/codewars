from random import randint
from unittest import TestCase

from kata.calculating_with_functions import (
    one, two, three, four, five, six, seven, eight, nine, zero, plus, minus, times, divided_by
)


class Test(TestCase):
    def test_fixed(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)

    def test_random(self):
        base_f = [zero, one, two, three, four, five, six, seven, eight, nine]

        for _ in range(40):
            a, b = randint(0, 9), randint(0, 9)
            self.assertEqual(base_f[a](plus(base_f[b]())), a + b)
            a, b = randint(0, 9), randint(0, 9)
            self.assertEqual(base_f[a](minus(base_f[b]())), a - b)
            a, b = randint(0, 9), randint(0, 9)
            self.assertEqual(base_f[a](times(base_f[b]())), a * b)
            a, b = randint(0, 9), randint(1, 9)
            self.assertEqual(base_f[a](divided_by(base_f[b]())), a // b)
