"""
This is an easy twist to the example kata (provided by Codewars when learning how to create your own kata).

Add the value "codewars" to the array websites 1,000 times.
"""

websites = []

# Solution 1
for i in range(0, 1000):
    websites.append("codewars")


# Solution 2
websites = ["codewars"] * 1000


# Solution 3
websites = ['codewars' for _ in range(1000)]