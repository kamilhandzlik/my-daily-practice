"""
Help the Fruit Guy

Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones.

Notes
If the array is null/nil/None or empty you should return empty array ([]).
The rotten fruit name will be in this camelcase (rottenFruit).
The returned array should be in lowercase.

user3028132
https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python
"""
# Solution 1
import re


# Solution 2
def remove_rotten(bag_of_fruits):
    return [re.sub('rotten', '', i).lower() for i in bag_of_fruits] if bag_of_fruits else []


# Solution 3
def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    return [fruit.replace("rotten", "").lower() for fruit in bag_of_fruits]


# Solution 4
def remove_rotten(bag_of_fruits):
    return list(map(lambda f: f.replace("rotten", "").lower(), bag_of_fruits)) if bag_of_fruits else []


# Solution 5
def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    return [fruit.removeprefix("rotten").lower() for fruit in bag_of_fruits]


# Solution 6
def remove_rotten(bag_of_fruits):
    return [] if not bag_of_fruits else [
        f.replace("rotten", "").lower() for f in bag_of_fruits
    ]


# Tests
import unittest
import random


class DefaultTest(unittest.TestCase):
    def rotten_removal_test(self):
        self.assertEqual(
            remove_rotten(["apple", "rottenBanana", "apple"]),
            ["apple", "banana", "apple"]
        )
        self.assertEqual(
            remove_rotten(["rottenApple", "rottenPear", "peach"]),
            ["apple", "pear", "peach"]
        )
        self.assertEqual(
            remove_rotten(["rottenOrange"]),
            ["orange"]
        )

    def empty_array_removal_test(self):
        self.assertEqual(remove_rotten([]), [])
        self.assertEqual(remove_rotten(None), [])
        self.assertEqual(remove_rotten([]), [])


class RandomTests(unittest.TestCase):
    def test_random(self):
        fruits = ["apple", "banana", "pear", "orange", "peach", "plum"]
        for _ in range(100):
            arr = []
            expected = []
            for _ in range(random.randint(0, 10)):
                fruit = random.choice(fruits)
                if random.random() < 0.5:
                    arr.append("rotten" + fruit.capitalize())
                    expected.append(fruit)
                else:
                    arr.append(fruit)
                    expected.append(fruit)
            self.assertEqual(remove_rotten(arr), expected)
