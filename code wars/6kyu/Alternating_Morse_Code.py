"""
Alternating Morse Code

Terminology
Morse code is a telecommunications method which encodes text characters as standardized sequences of two different signal durations, called dots and dashes.
For this task, we will consider a term "word" as any sequence of symbols.
Heterogram is a word, where each letter occurs only once.
Task
Implement a function alternating_morse_code(letter), which takes as an input an English uppercase letter and outputs a set of all heterograms starting with letter, such that, in their Morse code encoding, the dots and dashes alternate (

Notes
In order to prevent hardcoded solutions, your code's limit size needs to be less than 5000 characters.
MORSE_CODE preloaded dictionary is given to you, for a more convenient debugging.
"""

from preloaded import MORSE_CODE


def alternating_morse_code(letter: str) -> set[str]:
    letter = letter.upper()
    result = set()

    def dfs(word, used, last_signal):
        result.add(word)

        for l, morse in MORSE_CODE.items():
            if l in used:
                continue

            if last_signal and morse[0] == last_signal:
                continue

            ok = True
            for i in range(len(morse) - 1):
                if morse[i] == morse[i + 1]:
                    ok = False
                    break
            if not ok:
                continue

            dfs(
                word + l,
                used | {l},
                morse[-1]
            )

    start_morse = MORSE_CODE[letter]

    for i in range(len(start_morse) - 1):
        if start_morse[i] == start_morse[i + 1]:
            return set()

    dfs(letter, {letter}, start_morse[-1])
    return result
