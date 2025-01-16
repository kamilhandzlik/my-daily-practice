"""
Find the total sum of internal angles (in degrees) in an n-sided simple polygon.
N will be greater than 2.
"""

# Solution
def angle(n):
    if n <= 2:
        return "Error: A polygon must have at least 3 sides in Euclidean geometry."
    return (n - 2) * 180

# But for this kata you only need this
def angle(n):
    return (n - 2) * 180