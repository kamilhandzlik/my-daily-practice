"""
Largest 5 digit number in a series

In the following 6 digit number:

283910
91 is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 consecutive digits.

Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

Adapted from ProjectEuler.net
"""

def solution(digits: str) -> int:
    max_seq = 0

    for i in range(len(digits) - 4):
        current_seq = int(digits[i:i+5])
        if current_seq > max_seq:
            max_seq = current_seq

    return max_seq

import unittest
import random

class TestSolution(unittest.TestCase):
    def test_fixed_cases(self):
        cases = {
            "283910": 83910,
            "1234567890": 67890,
            "9876543210": 98765,
            "731674765": 74765,
            "9999999": 99999,
            "1234509876": 50987
        }
        for digits, expected in cases.items():
            with self.subTest(digits=digits):
                self.assertEqual(solution(digits), expected)

    def test_random_cases(self):
        for _ in range(10):
            digits = ''.join(str(random.randint(0, 9)) for _ in range(50))
            result = solution(digits)
            self.assertTrue(10000 <= result <= 99999)
            self.assertIn(str(result), digits)


if __name__ == "__main__":
    unittest.main()
