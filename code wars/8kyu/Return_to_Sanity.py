"""
Return to Sanity

This function should return an object, but it's not doing what's intended. What's wrong?

def mystery():
    results = {
    'sanity': 'Hello'}
    return
    results
"""

# Solution 1
def mystery():
    results = {
    'sanity': 'Hello'}
    return results


# Solution 2
def mystery():
    return {'sanity': 'Hello'}
