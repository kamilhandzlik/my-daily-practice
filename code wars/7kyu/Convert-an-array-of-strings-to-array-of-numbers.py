"""
Oh no!
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.
"""

# Solution 1
def to_float_array(arr):
    result = []
    for num in arr:
        if '.' not in num:
            result.append(int(num))
        else:
            result.append(float(num))
    return result


# Solution 2
def to_float_array(arr):
    return [int(num) if '.' not in num else float(num) for num in arr]

# Solution 3
def to_float_array(arr):
    return list(map(float, arr))


print(to_float_array(['1.1', '1.2', '1.3']))