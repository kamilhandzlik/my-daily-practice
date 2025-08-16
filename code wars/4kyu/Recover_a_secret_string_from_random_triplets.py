"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string,
recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere
before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets
and that they contain sufficient information to deduce the original string. In particular,
this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""
from collections import defaultdict, deque


def recover_secret(triplets):
    letters = set(char for triplet in triplets for char in triplet)
    graph = defaultdict(set)
    indegree = {char: 0 for char in letters}

    for a, b, c in triplets:
        for x, y in [(a, b), (b, c)]:
            if y not in graph[x]:
                graph[x].add(y)
                indegree[y] += 1

    result = []
    queue = deque(sorted([ch for ch in letters if indegree[ch] == 0]))

    while queue:
        ch = queue.popleft()
        result.append(ch)
        for neigh in sorted(graph[ch]):
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
        queue = deque(sorted(queue))

    return ''.join(result)


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]
print(recover_secret(triplets))
