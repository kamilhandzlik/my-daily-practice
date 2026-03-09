"""
Dashatize it

Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'

Dragoris
https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
"""


# Solution 1
def dashatize(n):
    dash = ''.join("-" + i + "-" if int(i) % 2 != 0 else i for i in str(n).strip('-'))
    return dash.replace('--', '-').strip('-')


# Solution 2
def dashatize(n):
    return ''.join("-" + i + "-" if int(i) % 2 != 0 else i for i in str(n).strip('-')).replace('--', '-').strip('-')


# Solution 3
import re


def dashatize(n):
    if n is None:
        return "None"
    s = str(abs(n))
    s = re.sub(r'([13579])', r'-\1-', s)
    return re.sub(r'-+', '-', s).strip('-')


# SoSolution 4
def dashatize(n):
    return ''.join(f"-{d}-" if int(d) % 2 else d for d in str(abs(n))).replace('--', '-').strip('-')


import unittest


class TestDashatize(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(dashatize(274), "2-7-4")
        self.assertEqual(dashatize(6815), "68-1-5")
        self.assertEqual(dashatize(0), "0")
        self.assertEqual(dashatize(1), "1")
        self.assertEqual(dashatize(5311), "5-3-1-1")
        self.assertEqual(dashatize(-5311), "5-3-1-1")
        self.assertEqual(dashatize(-1), "1")
        self.assertEqual(dashatize(86320), "86-3-20")
        self.assertEqual(dashatize(97531), "9-7-5-3-1")


def dash_ref(n):
    s = str(abs(n))
    out = []
    for ch in s:
        if int(ch) % 2:
            out.append(f"-{ch}-")
        else:
            out.append(ch)
    return ''.join(out).replace("--", "-").strip("-")


import random


class TestDashatizeRandom(unittest.TestCase):
    def test_random(self):
        for _ in range(200):
            n = random.randint(-10 ** 12, 10 ** 12)
            self.assertEqual(dashatize(n), dash_ref(n), f"Failed on n={n}")


if __name__ == "__main__":
    unittest.main()
