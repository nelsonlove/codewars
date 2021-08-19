from random import randint
from unittest import TestCase

from kata import pick_peaks


class Test(TestCase):
    def test_pick_peaks_fixed(self):
        self.assertEqual(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
        self.assertEqual(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
        self.assertEqual(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]),
                         {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]),
                         {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
        self.assertEqual(pick_peaks([]), {"pos": [], "peaks": []})
        self.assertEqual(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})

    def test_pick_peaks_random(self):
        def sol_peaks(arr):
            res = {"pos": [], "peaks": []}
            for i in range(1, len(arr) - 1):
                if arr[i - 1] < arr[i]:
                    temp = i
                    while arr[i] == arr[i + 1] and i < len(arr) - 2: i += 1
                    if arr[i] > arr[i + 1]:
                        res["pos"] += [temp]
                        res["peaks"] += [arr[temp]]
                    i += 1
                else:
                    i += 1
            return res

        for _ in range(100):
            arr = [randint(-5, 20) for x in range(randint(5, 30))]
            self.assertEqual(pick_peaks(arr[:]), sol_peaks(arr))
