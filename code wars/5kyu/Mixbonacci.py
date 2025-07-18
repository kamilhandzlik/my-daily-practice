"""
This is the first of my "-nacci" series. If you like this kata, check out the zozonacci sequence too.

Task
Mix -nacci sequences using a given pattern p.
Return the first n elements of the mixed sequence.
Rules
The pattern p is given as a list of strings (or array of symbols in Ruby) using the pattern mapping below (e. g. ['fib', 'pad', 'pel'] means take the next fibonacci, then the next padovan, then the next pell number and so on).
When n is 0 or p is empty return an empty list.
If n is more than the length of p repeat the pattern.
Examples
            0  1  2  3  4
----------+------------------
fibonacci:| 0, 1, 1, 2, 3 ...
padovan:  | 1, 0, 0, 1, 0 ...
pell:     | 0, 1, 2, 5, 12 ...

pattern = ['fib', 'pad', 'pel']
n = 6
#          ['fib',        'pad',      'pel',   'fib',        'pad',      'pel']
# result = [fibonacci(0), padovan(0), pell(0), fibonacci(1), padovan(1), pell(1)]
result = [0, 1, 0, 1, 0, 1]

pattern = ['fib', 'fib', 'pel']
n = 6
#          ['fib', 'fib', 'pel', 'fib', 'fib', 'pel']
# result = [fibonacci(0), fibonacci(1), pell(0), fibonacci(2), fibonacci(3), pell(1)]
result = [0, 1, 0, 1, 2, 1]
Sequences
fibonacci : 0, 1, 1, 2, 3 ...
padovan: 1, 0, 0, 1, 0 ...
jacobsthal: 0, 1, 1, 3, 5 ...
pell: 0, 1, 2, 5, 12 ...
tribonacci: 0, 0, 1, 1, 2 ...
tetranacci: 0, 0, 0, 1, 1 ...
Pattern mapping
'fib' -> fibonacci
'pad' -> padovan
'jac' -> jacobstahl
'pel' -> pell
'tri' -> tribonacci
'tet' -> tetranacci
If you like this kata, check out the zozonacci sequence.
"""


def fibonacci(n):
    seq = [0, 1]
    while len(seq) <= n:
        seq.append(seq[-1] + seq[-2])
    return seq[n]


def padovan(n):
    seq = [1, 0, 0]
    while len(seq) <= n:
        seq.append(seq[-2] + seq[-3])
    return seq[n]


def pell(n):
    seq = [0, 1]
    while len(seq) <= n:
        seq.append(2 * seq[-1] + seq[-2])
    return seq[n]


def jacobsthal(n):
    seq = [0, 1]
    while len(seq) <= n:
        seq.append(seq[-1] + 2 * seq[-2])
    return seq[n]


def tribonacci(n):
    seq = [0, 0, 1]
    while len(seq) <= n:
        seq.append(seq[-1] +seq[-2] + seq[-3])
    return seq[n]


def tetranacci(n):
    seq = [0, 0, 0, 1]
    while len(seq) <= n:
        seq.append(seq[-1] +seq[-2] + seq[ -3] + seq[-4])
    return seq[n]


sequence_funcs = {
    'fib': fibonacci,
    'pad': padovan,
    'pel': pell,
    'jac': jacobsthal,
    'tri': tribonacci,
    'tet': tetranacci
}


def mixbonacci(pattern, length):
    if not pattern or length==0:
        return []

    counters = {key: 0 for key in pattern}
    result = []

    for i in range(length):
        key = pattern[i% len(pattern)]
        func = sequence_funcs[key]
        result.append((func(counters[key])))
        counters[key] += 1

    return result