"""
Can you get the loop

You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:



# Use the `next' attribute to get the following node
node.next
Notes:

do NOT mutate the nodes!
in some cases there can be just a loop, with no dangling piece.
Don't miss dmitry's article in the discussion after you pass the Kata !!

Devouring
https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
"""

def loop_size(node):
    seen = set()
    cur = node
    while id(cur) not in seen:
        seen.add(id(cur))
        cur = cur.next
    entry = cur
    size = 1
    cur = cur.next
    while cur is not entry:
        cur = cur.next
        size += 1
    return size