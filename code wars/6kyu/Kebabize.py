"""
Kebabize

Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters

user4316848
https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
"""

# Solution 1
import re


def kebabize(st):
    s = re.sub(r"[0-9]", "", st)
    res = re.split(r'(?=[A-Z])', s)

    if not res:
        return res

    lres = [word.lower() for word in res]

    return '-'.join(filter(None, lres))


# Solution 2
import re


def kebabize(s):
    s = re.sub(r'\d+', '', s)
    s = re.sub(r'([A-Z])', r'-\1', s)
    return s.lower().lstrip('-')


# Solution 3
def kebabize(s):
    out = []
    for ch in s:
        if ch.isdigit():
            continue
        if ch.isupper():
            out.append('-')
            out.append(ch.lower())
        else:
            out.append(ch)
    res = ''.join(out)
    return res.lstrip('-')


print(kebabize('Code4Wars2'))
