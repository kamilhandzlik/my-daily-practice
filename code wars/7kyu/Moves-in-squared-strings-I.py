"""
This kata is the first of a sequence of four about "Squared Strings".

You are given a string of n lines, each substring being n characters long: For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
 hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"
or printed:

vertical mirror   |horizontal mirror
abcd --> dcba     |abcd --> mnop
efgh     hgfe     |efgh     ijkl
ijkl     lkji     |ijkl     efgh
mnop     ponm     |mnop     abcd
Task:
Write these two functions
and

high-order function oper(fct, s) where

fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)

Examples:
s = "abcd\nefgh\nijkl\nmnop"
oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"
Note:
The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Sample Tests".

Bash Note:
The input strings are separated by , instead of \n. The output strings should be separated by \r instead of \n. See "Sample Tests".


"""


# version 1
def vert_mirror(strng):
    s = strng.split('\n')
    reversed = []
    for i in s:
        reversed.append(i[::-1])
    return '\n'.join(reversed)


def hor_mirror(strng):
    split_strng = strng.split("\n")
    reversed_lines = split_strng[::-1]
    return '\n'.join(reversed_lines)


def oper(fct, s):
    if fct is not vert_mirror and fct is not hor_mirror:
        return "Error first argument must be either 'vert_mirror' or 'hor_mirror' function."
    elif fct is vert_mirror:
        return vert_mirror(s)
    else:
        return hor_mirror(s)


# version 2 - optimized
def vert_mirror(strng):
    return '\n'.join(i[::-1] for i in strng.split('\n'))


def hor_mirror(strng):
    split_strng = strng.split("\n")
    return '\n'.join(split_strng[::-1])


def oper(fct, s):
    if fct is vert_mirror:
        return vert_mirror(s)
    else:
        return hor_mirror(s)
