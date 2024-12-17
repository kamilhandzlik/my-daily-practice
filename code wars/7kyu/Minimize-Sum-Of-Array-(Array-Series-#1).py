"""
Introduction and Warm-up (Highly recommended)
Playing With Lists/Arrays Series
Task
Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

Notes
Array/list will contain positives only .
Array/list will always have even size
Input >> Output Examples
minSum({5,4,2,3}) ==> return (22)
Explanation:
The minimum sum obtained from summing each two integers product ,  5*2 + 3*4 = 22
minSum({12,6,10,26,3,24}) ==> return (342)
Explanation:
The minimum sum obtained from summing each two integers product ,  26*3 + 24*6 + 12*10 = 342
minSum({9,2,8,7,5,4,0,6}) ==> return (74)
Explanation:
The minimum sum obtained from summing each two integers product ,  9*0 + 8*2 +7*4 +6*5 = 74
Playing with Numbers Series
Playing With Lists/Arrays Series
For More Enjoyable Katas
ALL translations are welcomed
Enjoy Learning !!
Zizou
"""
import unittest

# Solution in python
def min_sum(arr):
    arr.sort()
    n = len(arr)

    mini_sum = 0
    for i in range(n // 2):
        mini_sum += arr[i] * arr[n - i - 1]

    return mini_sum

class TestMinSum(unittest.TestCase):
    def test_small_arrays(self):
        self.assertEqual(min_sum([5, 4, 2, 3]), 22, "Failed test case for array: [5, 4, 2, 3]")

    def test_medium_arrays(self):
        self.assertEqual(min_sum([12, 6, 10, 26, 3, 24]), 342, "Failed test case for array: [12, 6, 10, 26, 3, 24]")
        self.assertEqual(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74, "Failed test case for array: [9, 2, 8, 7, 5, 4, 0, 6]")

    def test_edge_cases(self):
        self.assertEqual(min_sum([1, 2, 1, 2]), 4, "Failed test case for array: [1, 2, 1, 2]")
        self.assertEqual(min_sum([10, 10, 10, 10]), 200, "Failed test case for array: [10, 10, 10, 10]")

    def test_large_arrays(self):
        self.assertEqual(min_sum([i for i in range(2, 102, 2)]), sum(i * j for i, j in zip(range(2, 52), range(100, 50, -2))), "Failed test case for large array")

if __name__ == "__main__":
    unittest.main()