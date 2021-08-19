from random import randint
from unittest import TestCase

from kata import max_sequence


class Test(TestCase):
    def test_max_sequence_fixed(self):
        self.assertEqual(max_sequence([]), 0,
                         'should work on an empty array')
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6,
                         'should work on the example')
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0,
                         'should work on the example with negative numbers')
        self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155,
                         'should work on this too')

    def test_max_sequence_random(self):
        def randomArray(size):
            return [randint(-30, 30) for i in range(0, size)]

        def max_sequence_sol(arr):
            lowest = ans = total = 0
            for i in arr:
                total += i
                lowest = min(lowest, total)
                ans = max(ans, total - lowest)
            return ans

        for i in range(50):
            ary = randomArray(50)
            self.assertEqual(max_sequence(ary[:]), max_sequence_sol(ary))
