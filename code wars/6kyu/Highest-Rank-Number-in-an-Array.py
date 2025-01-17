"""
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 1
"""


# Solution 1
def highest_rank(arr):
    m = 0
    res = arr[0]
    for i in arr:
        freq = arr.count(i)
        if freq > m or (freq == m and i > res):
            m = freq
            res = i
    return res


# Solution 2
def highest_rank(arr):
    counts = [[i, arr.count(i)] for i in set(arr)]
    max_freq = max(counts, key=lambda x: (x[1], x[0]))
    return max_freq[0]


# Solution 3
from collections import Counter


def highest_rank(arr):
    count = Counter(arr)
    max_freq = max(count.values())
    return max(k for k, v in count.items() if v == max_freq)


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
