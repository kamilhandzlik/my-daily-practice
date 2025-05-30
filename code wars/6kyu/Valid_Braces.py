"""
Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and
curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""


def valid_braces(string):
    st = []
    brace_map = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in "([{":
            st.append(char)
        elif char in ")]}":
            if not st or st[-1] != brace_map[char]:
                return False
            st.pop()
    return not st


print(valid_braces("()"))
print(valid_braces("(}"))
print(valid_braces("(){}[]"))
print(valid_braces("[(])"))
