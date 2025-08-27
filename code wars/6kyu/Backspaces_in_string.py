"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""


def clean_string(s):
    result = []

    for char in s:
        if char == '#':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)