"""
Error correction #1 - Hamming Code

Translations appreciated

Background information
The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works.
In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:

[ + ] It's simple to implement
[ + ] Compared to other versions of hamming code, we can correct more mistakes
[ - ] The size of the input triples
Task 1: Encode function
Implement the encode function, using the following steps:

convert every letter of the text to its ASCII value; (ASCII value of space is 32)
convert ASCII values to 8-bit binary;
triple every bit;
concatenate the result;
For example:

input: "hey"
--> 104, 101, 121                  // ASCII values
--> 01101000, 01100101, 01111001   // binary
--> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
--> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated
Task 2: Decode function:
Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:

111 --> 101 : this can and will happen
111 --> 11 : this cannot happen
Note: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

Steps:

Split the input into groups of three characters;
Check if an error occurred: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1, etc;
Take each group of 8 characters and convert that binary number;
Convert the binary values to decimal (ASCII);
Convert the ASCII values to characters and concatenate the result
For example:

input: "100111111000111001000010000111111000000111001111000111110110111000010111"
--> 100, 111, 111, 000, 111, 001, ...  // triples
-->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
--> 01101000, 01100101, 01111001       // bytes
--> 104, 101, 121                      // ASCII values
--> "hey"
If you liked this kata, please try out some of my other katas:
Crack the PIN
Decode the QR-Code
Hack the NSA
"""
from code_wars_kata_s import correct


# Solution 1
def encode(string):
    coded = [f"{ord(i):08b}" for i in string]
    tripled = []

    for i in coded:
        for char in i:
            tripled.append(char * 3)

    return ''.join(tripled)


def decode(bits):
    bits_split = [''.join(bits[i:i + 3]) for i in range(0, len(bits), 3)]
    error_check = []

    for i in bits_split:
        for char in i:
            if i.count(char) > 1:
                error_check.append(char)
                break

    joined = ''.join(error_check)
    return ''.join([chr(int(joined[i:i + 8], 2)) for i in range(0, len(joined), 8)])



# Solution 2
from collections import Counter

def encode(string):
    return ''.join(char * 3 for c in string for char in f"{ord(c):08b}")


def decode(bits):
    corrected = ''.join(Counter(bits[i:i+3]).most_common(1)[0][0] for i in range(0, len(bits), 3))
    return ''.join(chr(int(corrected[i:i+8], 2)) for i in range(0, len(corrected), 8))
