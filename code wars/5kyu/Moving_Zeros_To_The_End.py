"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""

# Solution 1 -> faster run only one run through list
def move_zeros(lst):
    list_without_zeroes = []
    number_of_zeroes = 0
    for i in lst:
        if i == 0:
            number_of_zeroes += 1
        else:
            list_without_zeroes.append(i)

    for j in range(0, number_of_zeroes):
        list_without_zeroes.append(0)
    return list_without_zeroes


# Solution 2 -> more fancy slightly slower does two runs through list
def move_zeros(lst):
    return [x for x in lst if x != 0] + [0] *lst.count(0)


# Overcomplicated way of using this code show output, expected and passed or failed all in different colours XD
print(f"""
Output: {move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])}\n
\033[33mExpected: [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]\033[0m\n
{'\033[32mPassed\033[0m' if move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]else 
'\033[31mFailed\033[0m'}
""")