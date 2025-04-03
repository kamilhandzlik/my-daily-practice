"""
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array. Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

Examples
[1, 2, 3] returns 6 because the maximum product is obtained from multiplying

2
∗
3
=
6
 2∗3=6
[9, 5, 10, 2, 24, -1, -48] returns 50 because the maximum product is obtained from multiplying

5
∗
10
=
50
 5∗10=50
[-23, 4, -5, 99, -27, 329, -2, 7, -921] returns -14 because the maximum product is obtained from multiplying

−
2
∗
7
=
−
14
 −2∗7=−14
"""

# Solurion 1
def adjacent_element_product(array):
    products = []

    for i, j in enumerate(array):
        if i == 0 or i+1 > len(array):
            product = 0
        else:
            product = j * array[i-1]
            products.append(product)

    max_product = max(products)
    return max_product


# Solurion 2
def adjacent_element_product(array):
    return max(a*b for a, b in zip(array, array[1:]))

print(f"{'✓' if  adjacent_element_product([5, 8]) == 40 else 'X'} test case: [5, 8] test result:{adjacent_element_product([5, 8])} expected: 40")
print(f"{'✓' if  adjacent_element_product([5, 1, 2, 3, 1, 4]) == 6 else 'X'} test case: [5, 1, 2, 3, 1, 4] test result:{adjacent_element_product([5, 1, 2, 3, 1, 4])} expected: 6")