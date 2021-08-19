from unittest import TestCase
from random import randint

from kata import array_diff


class Test(TestCase):
    def test_array_diff(self):
        self.basic_test_cases()
        self.random_test_cases()

    def basic_test_cases(self):
        self.assertEqual(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
        self.assertEqual(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

    def random_test_cases(self):
        def array_sol(a, b): return [item for item in a if item not in b]

        for _ in range(40):
            alen, blen = randint(0, 20), randint(0, 20)
            a = [randint(0, 40) - 20 for i in range(alen)]
            b = [randint(0, 40) - 20 for i in range(blen)]
            exp = array_sol(a[:], b[:])
            self.assertEqual(array_diff(a[:], b[:]), exp)
