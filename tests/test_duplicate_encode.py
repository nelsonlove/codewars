from random import randint
from unittest import TestCase

from kata import duplicate_encode


class Test(TestCase):
    def test_duplicate_encode_basic(self):
        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEqual(duplicate_encode("CodeWarrior"), "()(((())())")
        self.assertEqual(duplicate_encode("Supralapsarian"), ")()))()))))()(", "should ignore case")
        self.assertEqual(duplicate_encode("iiiiii"), "))))))", "duplicate-only-string")

        # Tests with '(' and ')'
        self.assertEqual(duplicate_encode("(( @"), "))((")
        self.assertEqual(duplicate_encode(" ( ( )"), ")))))(")

    def test_duplicate_encode_random(self):
        def duplicate_sol(word):
            return "".join(["(" if word.lower().count(x.lower()) == 1 else ")" for x in word])

        for _ in range(40):
            testlen = randint(6, 40)
            testword = ""
            for i in range(testlen):
                letter = "abcdefghijklmnopqrstuvwxyz() @!"[randint(0, 30)]
                testword += letter if randint(0, 1) == 0 else letter.upper()
            self.assertEqual(duplicate_encode(testword),
                             duplicate_sol(testword),
                             "It Should encode '" + duplicate_sol(testword) + "'"
                             )
