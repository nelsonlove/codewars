from unittest import TestCase

from kata import unique_in_order


class Test(TestCase):
    def test_unique_in_order(self):
        self.assertEqual(unique_in_order(''), [], "should work with empty array")
        self.assertEqual(unique_in_order('A'), ['A'], "should work with one element")
        self.assertEqual(unique_in_order('AA'), ['A'], "should reduce duplicates")
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('AADD'), ['A', 'D'])
        self.assertEqual(unique_in_order('AAD'), ['A', 'D'])
        self.assertEqual(unique_in_order('ADD'), ['A', 'D'])
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'],
                         "should treat lowercase as different from uppercase")
        self.assertEqual(unique_in_order([1, 2, 3, 3]), [1, 2, 3],
                         "should work with int arrays")
        self.assertEqual(unique_in_order(['a', 'b', 'b']), ['a', 'b'],
                         "should work with char arrays")
