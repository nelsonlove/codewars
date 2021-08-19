from unittest import TestCase

from kata import filter_list


class Test(TestCase):
    def test_filter_list(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])
        self.assertEqual(filter_list(['a', 'b', '1']), [])
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
