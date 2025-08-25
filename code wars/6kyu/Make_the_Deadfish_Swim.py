"""
 Create a parser to interpret and execute the Deadfish language.
Deadfish operates on a single value in memory, which is initially set to 0.
It uses four single-character commands:
i: Increment the value d: Decrement the value s: Square the value o: Output the value to a result array All other instructions are no-ops and have no effect.
Examples Program "iiisdoso" should return numbers [8, 64]. Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
"""


def parse(data):
    value = 0
    output = []

    for command in data:
        if command == 'i':
            value += 1
        elif command == 'd':
            value -= 1
        elif command == 's':
            value *= value
        elif command == 'o':
            output.append(value)

    return output