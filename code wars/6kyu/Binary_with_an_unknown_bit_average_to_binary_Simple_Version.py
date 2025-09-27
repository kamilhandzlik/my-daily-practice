"""
Binary with an unknown bit: average to binary (Simple Version)

This Kata is intended to be a simple version of Binary with unknown bits: average to binary.

The main difference is that in this Kata, input n will only be an integer, and only consider those binary string with exactly one x (or cases of 0 and 1).

After work out the pattern for this Kata, you can try to work out the pattern for 2 or more xs, also the cases of integer + 0.5 for the above linked Kata.

There are many different approaches other than this one for the other Kata.

Background
In another Kata you calculated the average number from a string of binary with unknown bits, using the rules (see rules section below).

We now define average as the result calculated in the way described in that Kata.

Average to Binary
You need the original binary strings, but somebody deleted them, there is no way to get them back.

The only solution is to use the average n to find the original binary strings.

Also, we know that the orginal binary strings has exactly one x in it.

It looks like this:

average => string

4 => 'x00'
5 => '1x0'
5 => 'x01'
But some numbers will result in more than one strings.

So we collect all strings for the input into a set.

It looks like this:

average => set of strings

4 => {'x00'}
5 => {'1x0', 'x01'}
And the task of this Kata is to write the function which takes the number n and returns the set.

Task:
You will get a non-negative integer n as input.

Find all the strings with exactly one x in it: for each string, its average would equal to the input n.

Return a set of all strings found.

Rules:
The string consists of 0, 1 and/or x, if its length is 2 or higher, it would have exactly one x.

Unless the number is a single zero(0), otherwise no leading zeros are allowed.

x can be 0 or 1, but the string has to follow the above rules.

Performance
small tests: 30 tests of numbers up to 2^20

Med Tests: 30 tests of numbers up to 2^30

BIG TESTS: 30 tests of numbers up to 2^40

*E*X*T*R*A* *T*E*S*T*S*: 10 tests of numbers up to 2^50

Example
Input n = 25

25 => average of 25 => '11001' => 'x1001'

                              24:'11000'
25 => average of 24 and 26 => 26:'11010' => '110x0'
                        result > '110x0'

                              21:'10101'
25 => average of 21 and 29 => 29:'11101' => '1x101'
                        result > '1x101'

The set of 25 is {'110x0', '1x101', 'x1001'}.
Sample Tests
0 => {'0'}
1 => {'1'}
2 => {'x0'}
3 => {'x1'}
4 => {'x00'}
5 => {'1x0', 'x01'}
6 => {'1x1', 'x10'}
25 => {'110x0', '1x101', 'x1001'}
1572864 => {'x10000000000000000000', '1x1000000000000000000'}
Don't ask what happened to the guy who deleted the original strings, it is a horrible story.
"""


def average_to_binary(n):
    if n in (0, 1):
        return {str(n)}

    result = set()
    bin_n = bin(n)[2:]


    if len(bin_n) >= 2:
        result.add('x' + bin_n[1:])

    L = len(bin_n)
    for p in range(1, L + 1):
        d = 1 << (p - 1)
        a = n - d
        b = n + d
        if a < 0:
            continue
        if (a ^ b) != (1 << p):
            continue
        a_bin = bin(a)[2:]
        b_bin = bin(b)[2:]
        if len(a_bin) != len(b_bin):
            continue
        if a_bin[0] != '1' or b_bin[0] != '1':
            continue
        idx = len(b_bin) - 1 - p
        if not (0 <= idx < len(b_bin)):
            continue
        candidate = b_bin[:idx] + 'x' + b_bin[idx + 1:]
        result.add(candidate)

    return result
