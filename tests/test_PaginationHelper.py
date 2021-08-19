from unittest import TestCase

from kata import PaginationHelper


class TestPaginationHelper(TestCase):
    def setUp(self):
        collection = range(1, 25)
        self.helper = PaginationHelper(collection, 10)

    def test_item_count(self):
        self.assertEqual(self.helper.item_count(), 24, 'item_count returned incorrect value')

    def test_page_count(self):
        self.assertEqual(self.helper.page_count(), 3, 'page_count is returning incorrect value.')

    def test_page_item_count(self):
        self.assertEqual(self.helper.page_item_count(1), 10, 'page_item_count is returning incorrect value.')
        self.assertEqual(self.helper.page_item_count(2), 4, 'page_item_count is returning incorrect value')
        self.assertEqual(self.helper.page_item_count(3), -1, 'page_item_count is returning incorrect value')

    def test_page_index(self):
        self.assertEqual(self.helper.page_index(0), 0, 'page_index returned incorrect value')
        self.assertEqual(self.helper.page_index(23), 2, 'page_index returned incorrect value')
        self.assertEqual(self.helper.page_index(24), -1,
                         'page_index returned incorrect value when provided a item_index argument that was out of '
                         'range')
        self.assertEqual(self.helper.page_index(40), -1,
                         'page_index returned incorrect value when provided a item_index argument that was out of '
                         'range')
        self.assertEqual(self.helper.page_index(3), 0, 'page_index returned incorrect value')
        self.assertEqual(self.helper.page_index(-1), -1,
                         'page_index returned incorrect value when provided a itemIndex argument that was out of '
                         'range. pageIndex(-1) should return -1')
        self.assertEqual(self.helper.page_index(-23), -1,
                         'page_index returned incorrect value when provided a item_index argument that was out of '
                         'range. pageIndex(-23) shoudl return -1')
        self.assertEqual(self.helper.page_index(-15), -1,
                         'page_index returned incorrect value when provided a item_index argument that was out of '
                         'range.')

    def test_empty_array(self):
        helper = PaginationHelper([], 10)
        self.assertEqual(helper.page_index(0), -1, 'pageIndex(0) called when there was an empty collection')
