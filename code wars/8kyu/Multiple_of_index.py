"""
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
"""

# First solution that came to my mind and it is crude but works time to optimalize it and made sure to keep it with good practises
def multiple_of_index(arr):
    if 0 not in arr:
        return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
    elif arr[0] == 0:
        moi =  [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
        moi.insert(0, 0)
        return moi
    else:
        return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


# Better solution
def multiple_of_index(arr):
    result = []
    if arr[0] == 0:
        result.append(0)

    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            result.append(arr[i])

    return result


# good solution
def multiple_of_index(arr):
    return [j for i,j in enumerate(arr) if (j==0 and i==0) or (i!=0 and j%i==0)]

print(multiple_of_index([22, -6, 32, 82, 9, 25]))
print(multiple_of_index([0, 2, 3, 6, 9]))