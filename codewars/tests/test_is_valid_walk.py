from random import randint, choice
from unittest import TestCase

from kata import is_valid_walk

passwalk = [['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'],
            ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'], ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']]
failwalk = [['n'], ['n', 's'], ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'],
            ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's', 'e', 'w'],
            ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'n'], ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']]


class Test(TestCase):
    def test_is_valid_walk_basic(self):
        self.assertTrue(not is_valid_walk(failwalk[0][:]), "should return false if walk is too short")
        self.assertTrue(not is_valid_walk(failwalk[1][:]), "should return false if walk is too short")
        self.assertTrue(not is_valid_walk(failwalk[2][:]), "should return false if walk is too long")
        self.assertTrue(not is_valid_walk(failwalk[3][:]), "should return false if walk is too long")
        self.assertTrue(not is_valid_walk(failwalk[4][:]),
                        "should return false if walk does not bring you back to start")
        self.assertTrue(not is_valid_walk(failwalk[5][:]),
                        "should return false if walk does not bring you back to start")
        self.assertTrue(is_valid_walk(passwalk[0][:]), "should return true for a valid walk")
        self.assertTrue(is_valid_walk(passwalk[1][:]), "should return true for a valid walk")
        self.assertTrue(is_valid_walk(passwalk[2][:]), "should return true for a valid walk")
        self.assertTrue(is_valid_walk(passwalk[3][:]), "should return true for a valid walk")

    def test_is_valid_walk_random(self):
        def valid_sol(walk):
            return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

        for i in range(0, 100):
            number = randint(1, 7)
            testw = passwalk[number % 4]
            if number < 4:
                testw[randint(0, 9)] = ['n', 's', 'w', 'e'][randint(0, 3)]
            self.assertEqual(is_valid_walk(testw[:]), valid_sol(testw),
                             "It should work also for a " + str(testw) + " walk")
        for i in range(100):
            testw = [choice('nswe') for _ in range(randint(4, 5))]
            testw += ['snew'['nswe'.index(c)] for c in testw]
            if randint(0, 1) == 0:
                testw[0] = 'swen'['nswe'.index(testw[0])]
            self.assertEqual(is_valid_walk(testw[:]), valid_sol(testw),
                             "It should work also for a " + str(testw) + " walk")
