"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""
# Solution 1
import re

def to_camel_case(text):
    if not text:
        return ""

    words = re.split(r'[-_]', text)
    cc = []

    for word in words:
        if word == words[0]:
            cc.append(word)
        else:
            cc.append(word.capitalize())
    return "".join(cc)


# Solution 2
import re

def to_camel_case(text):
    return "" if not text else "".join([word if word == re.split(r'[-_]', text)[0] else word.capitalize() for word in re.split(r'[-_]', text)])


# Solution 3 XD
import re; to_camel_case = lambda t: (s:=re.split(r'[-_]',t)) and s[0]+''.join(map(str.title,s[1:])) or ''

# Solution 4
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')