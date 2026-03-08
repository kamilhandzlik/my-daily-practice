"""
L1: Set Alarm

Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

employed | vacation
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false

Swolebrain
https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
"""


# Solution 1
def set_alarm(employed, vacation):
    if employed and vacation:
        return False
    elif not employed and vacation:
        return False
    elif not employed and not vacation:
        return False
    else:
        return True


# Solution 2
def set_alarm(employed, vacation):
    rules = {(True, True): False, (False, True): False, (False, False): False, (True, False): True}
    return rules[(employed, vacation)]


# Solution 3
def set_alarm(employed, vacation):
    return employed and not vacation


# Solution 4
def set_alarm(employed, vacation):
    return employed and not vacation or False


# Solution 5
def set_alarm(employed, vacation):
    return bool(employed and not vacation)


# Solution 6
set_alarm = lambda employed, vacation: employed and not vacation


# Solution 7
def set_alarm(employed, vacation):
    table = [
        [False, False],  # employed = False
        [True, False]  # employed = True
    ]
    return table[employed][vacation]


# Testy
import unittest
import random

class TestSetAlarm(unittest.TestCase):
    def test_basic_cases(self):
        self.assertFalse(set_alarm(True, True))
        self.assertTrue(set_alarm(True, False))
        self.assertFalse(set_alarm(False, True))
        self.assertFalse(set_alarm(False, False))

    def test_types(self):
        self.assertIsInstance(set_alarm(True, False), bool)
        self.assertIsInstance(set_alarm(False, False), bool)


def reference_solution(employed, vacation):
    return employed and not vacation

class TestRandom(unittest.TestCase):
    def test_random(self):
        for _ in range(100):
            employed = random.choice([True, False])
            vacation = random.choice([True, False])
            self.assertEqual(set_alarm(employed, vacation), reference_solution(employed, vacation))

if __name__ == "__main__":
    unittest.main()
