import unittest
from random import randint, randrange, getrandbits

def div_con(x):
    """
    Given a mixed array of number and string representations of integers, 
    add up the non-string integers and subtract the total of the string integers.
    """
    str_sum = sum(int(i) for i in x if isinstance(i, str))
    int_sum = sum(i for i in x if isinstance(i, int))
    return int_sum - str_sum

# Predefined test cases
div_con_test_cases = {
    (9, 3, '7', '3'): 2,
    ('5', '0', 9, 3, 2, 1, '9', 6, 7): 14,
    ('3', 6, 6, 0, '5', 8, 5, '6', 2, '0'): 13,
    ('1', '5', '8', 8, 9, 9, 2, '3'): 11,
    (8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7): 61,
}

def generate_random_test_div_con():
    """Generates a random test case for div_con function."""
    length = randrange(1, 101)  # Random length between 1 and 100
    test_case = [str(randint(0, 1000)) if getrandbits(1) else randint(0, 1000) for _ in range(length)]
    return test_case

class DivConTest(unittest.TestCase):
    def test_predefined_cases(self):
        """Tests the div_con function with predefined test cases."""
        for x, expected in div_con_test_cases.items():
            with self.subTest(x=x, expected=expected):
                self.assertEqual(div_con(list(x)), expected)

    def test_random_cases(self):
        """Tests the div_con function with 30 random test cases."""
        for _ in range(30):
            test_case = generate_random_test_div_con()
            # Calculate expected result manually
            expected = sum(i for i in test_case if isinstance(i, int)) - sum(int(i) for i in test_case if isinstance(i, str))
            with self.subTest(test_case=test_case):
                self.assertEqual(div_con(test_case), expected)

if __name__ == '__main__':
    unittest.main()
