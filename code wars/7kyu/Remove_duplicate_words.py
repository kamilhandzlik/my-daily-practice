"""
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
"""

def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in s.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)


print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))