"""
You have to write a function that describe Leo:

def leo(oscar):
  pass
if oscar was (integer) 88, you have to return "Leo finally won the oscar! Leo is happy".
if oscar was 86, you have to return "Not even for Wolf of wallstreet?!"
if it was not 88 or 86 (and below 88) you should return "When will you give Leo an Oscar?"
if it was over 88 you should return "Leo got one already!"
"""


# Solution 1
def leo(oscar):
    if oscar > 88:
        return "Leo got one already!"
    elif oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    else:
        return "When will you give Leo an Oscar?"


# Solution 2
def leo(oscar):
    return "Leo got one already!" if oscar > 88 else "Leo finally won the oscar! Leo is happy" \
        if oscar == 88 else "Not even for Wolf of wallstreet?!" if oscar == 86 else "When will you give Leo an Oscar?"


# Solution 3 -  without using if statement
def leo(oscar):
    responses = [
        "When will you give Leo an Oscar?",
        "Not even for Wolf of wallstreet?!",
        "Leo finally won the oscar! Leo is happy",
        "Leo got one already!"
    ]

    index = (oscar == 86) * 1 + (oscar == 88) * 2 + (oscar > 88) * 3
    return responses[index]