"""
Don't Drink the Water

Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

{                             {
  { 'H', 'H', 'W', 'O' },        { 'O','O','O','O' },
  { 'W', 'W', 'O', 'W' },  =>    { 'W','W','W','W' },
  { 'H', 'H', 'O', 'O' }         { 'H','H','H','H' }
}                             }

NateBrady23
https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python
"""


def separate_liquids(glass):
    if not glass:
        return []

    density = {
        "H": 1.36,
        "W": 1.00,
        "A": 0.87,
        "O": 0.80
    }
    flat = [cell for row in glass for cell in row]
    flat.sort(key=lambda x: density[x])

    width = len(glass[0])
    return [flat[i:i+width] for i in range(0, len(flat), width)]





