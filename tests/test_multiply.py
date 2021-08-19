from unittest import TestCase

from kata import multiply


class Test(TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(1.5, 2.5), 3.75)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)
