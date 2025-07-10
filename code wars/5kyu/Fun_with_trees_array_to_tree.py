"""
You are given an array of integers. Implement a function which creates a complete binary tree from the array (complete meaning that every level of the tree, except possibly the last, is completely filled).

The elements of the array are to be taken left-to-right, and put into the tree top-to-bottom, left-to-right.

For example, given the array [17, 0, -4, 3, 15] you should create the following tree:

    17
   /  \
  0   -4
 / \
3   15
A tree node type is preloaded for you:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
This kata is part of fun with trees series:

Fun with trees: max sum
Fun with trees: array to tree
Fun with trees: is perfect
"""

from preloaded import Node
from collections import deque


def array_to_tree(arr):
    if not arr:
        return None

    root = Node(arr[0])
    queue = deque([root])
    i = 1

    while i < len(arr):
        current = queue.popleft()

        if i < len(arr):
            current.left = Node(arr[i])
            queue.append(current.left)
            i += 1

        if i < len(arr):
            current.right = Node(arr[i])
            queue.append(current.right)
            i += 1

    return root
