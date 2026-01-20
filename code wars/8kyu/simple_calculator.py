"""
simple calculator

You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

You should return the result of applying the given operation to these numbers.

Note: In dynamically typed languages (JS, PHP, Python), the first and second arguments can be not numbers. In that case, return "unknown value".

If the given operation to perform on the two numbers is not one of the four mentioned above, you should:

return a value:
"unknown value" (JS, PHP, Python)
throw an exception:
std::invalid_argument (C++)
ArgumentException (C#)
IllegalArgumentException (Java)
Example:
arguments: 1, 2, "+"
should return 3

arguments: 1, 2, "&"
refer to the description for what you should return in this case

# Specifically for dynamically-typed languages:

arguments: 1, "k", "*"
should return "unknown value"
Good luck!

"""


# Solution 1
def calculator(x, y, op):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"


# Solution 2
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculator(x, y, op):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return ops[op](x, y) if op in ops else "unknown value"
    else:
        return "unknown value"


# Solution 3
def calculator(x, y, op):
    if not all(isinstance(v, (int, float)) for v in (x, y)):
        return "unknown value"

    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    return ops.get(op, lambda *_: "unknown value")(x, y)


# Solution 4
def calculator(x, y, op):
    ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}
    return ops.get(op, lambda *_: "unknown value")(x, y) if isinstance(x, (int, float)) and isinstance(y, (
    int, float)) else "unknown value"
