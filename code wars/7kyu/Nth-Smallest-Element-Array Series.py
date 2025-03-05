"""
Introduction and warm-up (highly recommended): Playing With Lists/Arrays Series

Task
Given an array/list of integers, find the Nth smallest element in the array.

Notes
Array/list size is at least 3.
Array/list's numbers could be a mixture of positives , negatives and zeros.
Repetition in array/list's numbers could occur, so don't remove duplications.
Input >> Output Examples
arr=[3,1,2]            n=2    ==> return 2
arr=[15,20,7,10,4,3]   n=3    ==> return 7
arr=[2,169,13,-5,0,-1] n=4    ==> return 2
arr=[2,1,3,3,1,2],     n=3    ==> return 2
Playing with Numbers Series
Playing With Lists/Arrays Series
More Enjoyable Katas
Enjoy Learning !!
"""

# Version 1
def nth_smallest(arr, pos):
    current = 0
    new_list = arr

    while current < pos - 1:
        smallest_element = min(new_list)
        current += 1
        new_list.remove(smallest_element)

    return min(new_list)


# Version 2
def nth_smallest(arr, pos):
    arr.sort()
    return arr[pos - 1]


print(nth_smallest([-102,-16,-1,-2,-367,-9],5))