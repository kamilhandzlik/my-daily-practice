"""
Who ate the cookie

For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.

Please leave feedback for this kata. Cheers!
"""

# Solution 1
def cookie(x):
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    elif isinstance(x, (float, int)) and not isinstance(x, bool):
        return 'Who ate the last cookie? It was Monica!'
    else:
        return  'Who ate the last cookie? It was the dog!'

# Solution 2
def cookie(x):
    return f"Who ate the last cookie? It was {'Zach' if isinstance(x, str) else 'Monica' if isinstance(x, (float, int)) and not isinstance(x, bool) else 'the dog'}!"

# Solution 3
def cookie(x):
    name = 'Zach' if isinstance(x, str) else 'Monica' if isinstance(x, (float, int)) and not isinstance(x, bool) else 'the dog'
    return f"Who ate the last cookie? It was {name}!"

# Solution 4 XD
def cookie(x):
    type_map = {
        str: "Zach",
        int: "Monica",
        float: "Monica"
    }
    name = type_map.get(type(x), "the dog") if not isinstance(x, bool) else "the dog"
    return f"Who ate the last cookie? It was {name}!"


print(cookie(True))