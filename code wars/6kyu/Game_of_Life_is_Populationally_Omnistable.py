"""
Conway's Game of Life is a 2D cellular automaton. You can read the rules here if unfamiliar.

A still life is an oscillator with period 1. In other words, a set of cells that does not change
over time and has a single state. The examples include:

Name	Size	Image
Block	2x2
Beehive with tail	5x6
Still lifes can be composed of any number of islands. Each of those islands has a neigborhood - a union
of neighborhoods of its cells. Two islands are considered linked if their neighborhoods are overlapping.
Given that there might be any number of islands, their links can be summarized in a graph.
Strict still lifes are based on this concept. For a still life to be strict, it must satisfy these two rules:

Island linkage graph must be connected. In other words: no structures that don't influence each other.
Any non-empty proper subset of its islands must not be still. In other words: no lifes that are still on their own.
Name	Size	Is Strict	Image
Block (1 island)	2x2	Yes
Duplicated block (2 islands, linked)	2x5	No
Duplicated block (2 islands, not linked)	2x6	No
Mirrored table (two islands, linked)	4x5	Yes
Explaination:

A single block has a single island. There are no non-empty proper subsets of set with 1 element,
so connected still lifes are always strict.
Two blocks, no matter do they overlap or not, are still lifes on their own,
therefore their combination is not strict.- A mirrored table has two islands and they are connected,
so the first condition is true. One table is not stable without the other, and besides 1 out of 2 tables
there are no more proper non-empty subsets. So the second condition is also true and a mirrored table is strict.
Objective
Given a non-negative integer N produce a strict still life with N cells. N can not be 1, 2, 3, but can be 0, 4, 5, etc.
Represent the answer as a list of alive cells. Your code will be tested against N up to 2000.
"""

# Solution
def create_still_life_with_population(n):
    s = []
    for i in range(0,n//2): s+=[(i,i+1),(i+1,i)]
    return s+[(0,0)] if n%2 else s



