"""
Even or Odd Accessor

Create a function or callable object that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers. The function should also return "Even" or "Odd" when accessing a value at an integer index.

For example:

evenOrOdd(2); //'Even'
evenOrOdd[2]; //'Even'
evenOrOdd(7); //'Odd'
evenOrOdd[7]; //'Odd'

MissinqLink
https://www.codewars.com/kata/6656a4687f3e4eb5fb520817/train/python
"""


class EvenOrOdd:
    def __call__(self, number):
        return "Odd" if number % 2 else "Even"

    def __getitem__(self, number):
        return "Odd" if number % 2 else "Even"

even_or_odd = EvenOrOdd()