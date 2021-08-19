from random import randint, shuffle
from unittest import TestCase

from kata import strip_comments


class Test(TestCase):
    def test_strip_comments_basic(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas #!apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\navocado @apples", ["@", "!"]),
                         "apples, pears # and bananas\ngrapes\navocado")
        self.assertEqual(strip_comments("apples, pears § and bananas\ngrapes\navocado *apples", ["*", "§"]),
                         "apples, pears\ngrapes\navocado")
        self.assertEqual(strip_comments("", ["#", "!"]), "")
        self.assertEqual(strip_comments("#", ["#", "!"]), "")
        self.assertEqual(strip_comments("\n§", ["#", "§"]), "\n")
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", []),
                         "apples, pears # and bananas\ngrapes\nbananas !apples")

    def test_strip_comments_random(self):
        symbols = ["@", "#", "!", "?", "'", "^", ".", ",", "=", "-"]
        fruits = ["avocados", "pears", "apples", "bananas", "cherries", "strawberries", "oranges", "lemons",
                  "watermelons"]

        def test_solution(input, markers):
            res = input[:].split("\n")
            for i in range(len(res)):
                for symbol in markers:
                    if symbol in res[i]: res[i] = res[i][:res[i].index(symbol)]
                res[i] = res[i].rstrip()
            return "\n".join(res)

        for i in range(40):
            test_string = "\n".join([" ".join(
                [fruits[randint(0, len(fruits) - 1)] if randint(1, 10) < 9 else symbols[randint(0, len(symbols) - 1)]
                 for i in range(randint(1, 6))]) for z in range(randint(3, 5))])
            shuffle(symbols)
            markers = symbols[:randint(0, len(symbols) - 1)]
            self.assertEqual(strip_comments(test_string, markers), test_solution(test_string[:], markers),
                             "It should work with random inputs too")
