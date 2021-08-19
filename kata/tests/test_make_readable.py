from random import randint
from unittest import TestCase

from kata import make_readable


class Test(TestCase):
    def test_make_readable(self):
        def make_readable_solution(seconds):
            return "{:02}:{:02}:{:02}".format(seconds // 3600, seconds // 60 % 60,
                                              seconds % 60)

        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(59), "00:00:59")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(3599), "00:59:59")
        self.assertEqual(make_readable(3600), "01:00:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(86400), "24:00:00")
        self.assertEqual(make_readable(359999), "99:59:59")

        for i in range(100):
            random_number = randint(0, 359999)
            self.assertEqual(make_readable(random_number), make_readable_solution(random_number))
