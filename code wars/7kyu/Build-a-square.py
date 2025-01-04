"""
I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer will be a whole number between 1 and 50.

Example
n = 3, so I expect a 3x3 square back just like below as a string:

+++
+++
+++
"""


# Solution 1
def generate_shape(n):
    rows = []
    for _ in range(n):
        rows.append('+' * n)
    i = ('\n').join(rows)
    return i

# Solution 2
def generate_shape(n):
    return ('\n').join(['+' * n for _ in range(n)])