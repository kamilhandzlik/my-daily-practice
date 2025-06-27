"""
Introduction
A one-instruction set computer (OISC) is an abstract machine that uses only one instruction, obviating the need for a machine language opcode.

Subleq (Subtract and Branch if Less than or Equal to Zero) is a turing-complete OISC. Your task is to write programs for this architecture to perform various operations.

Subleq Instruction:
Each Subleq instruction has 3 memory address operands

Instruction subleq a, b, c
    Mem[b] = Mem[b] - Mem[a]
    if (Mem[b] ≤ 0)
        goto c
Implementation:
In this kata, address -1 is always 0. Writing to it (subleq a, -1, c) writes mem[a] to the output of the program and jumps to c.
Your program will be loaded in memory starting at address 0, and the program counter will be initialized as 0.
The inputs of your program will be loaded into negative address of the memory. Your program can only access the allocated memory.
def subleq_interpreter(program: list[int], mem: dict[int, int]):

    mem[-1] = 0

    # load program into memory
    for i, v in enumerate(program):
        mem[i] = v

    out = []
    pc = 0  # program counter
    while pc != -1:
        try:
            a, b, c = mem[pc], mem[pc + 1], mem[pc + 2]
            if b == -1:
                out.append(mem[a])
            else:
                mem[b] -= mem[a]
            if mem[b] <= 0:
                pc = c
            else:
                pc += 3
        except KeyError as e:
            raise SegmentationFaultError(e.args[0])
    return out
Examples :
Addition
This program adds the values at addresses -2 and -3 (A and B), and outputs the result: [-2, 9, 3, 9, -3, 6, -3, -1, -1, 0]

pseudocode:

x = 0
x -= A
B -= x
return B
We group the instructions 3 by 3 to break down the execution:

0:  -2,  9,  3,   ; mem[9] -= mem[-2], go to 3  (now mem[9] = -A)
3:   9, -3,  6,   ; mem[-3] -= mem[9], go to 6  (now mem[-3] = -(A+B))
6:  -3, -1, -1,   ; Output mem[-3] and jump to address -1 (output the sum and halt)
9:   0,           ; used as storage (x)
Counting
This program outputs numbers from 0 up to the value at address -2 (excluded) : [16, -2, -1, 15, -1, 6, 17, -2, 9, 18, 15, 12, 16, 16, 0, 0, 0, 1, -1]

here we use the address 15 as an increasing counter
and addresses 16, 17, 18 as constants with respective values 0, 1, -1

Grouped instructions:

0:   16, -2, -1,   ; if mem[-2] <= 0 go to -1 (halt)
3:   15, -1,  6,   ; output mem[15] (our counter)
6:   17, -2,  9,   ; mem[-2] -= 1
9:   18, 15, 12,   ; mem[15] += 1
12:  16, 16,  0,   ; jump to 0
15:   0,  0,  1,   ; used as storage
18:  -1,           ; used as storage
Tasks
1. Multiplication
Write a program that multiplies values in addresses -2 and -3, writing the result to output. Input values can be negative.

2. Division
Write a program that performs division with remainder:

address -2: Dividend, >= 0
address -3: Divisor, > 0
output: [quotient, remainder]
3. String Printer
Create a function that generates a SUBLEQ program to output a given string:

def print_string(s: str) -> list[int]:
    # returns a SUBLEQ program that prints s
For this program outputing a value v is considered printing the character chr(v) with the corresponding ASCII code.
The output of the program should then verify "".join(map(chr, output)) == s
Your program will be tested with ASCII printable characters (codes 32-126).

4. Buffer Copier
Create a SUBLEQ program that copies a buffer:

address -4: contains the source buffer address
address -3: contains the buffer size
address -2: contains the destination buffer address
Your program should override the data of the destination buffer with a copy of the source buffer, and the source buffer should be left unchanged.
"""


multiply = [
    57, -2, 15,
    57, -2, 51,
    -3, 57, 9,
    59, -2, 51,
    58, 58, 6,
    -2, 57, 18,
    -2, -2, 21,
    57, 58, 24,
    58, -2, 27,
    57, 57, 30,
    58, 58, 33,
    -3, 57, 36,
    -3, -3, 39,
    57, 58, 42,
    58, -3, 45,
    57, 57, 48,
    58, 58, 3,
    57, 58, 54,
    58, -1, -1,
    0, 0, 1
]

divide = [
    13, -2, 1,
    -3, -2, 9,
    2, 27, 3,
    27, 28, 12,
    28, -1, 15,
    2, -2, 18,
    -2, 29, 21,
    29, -3, 24,
    -3, -1, -1,
    0,
    0,
    0,
]

def print_string(s):
    return [
        0, 15, -1,
        15, -1, 6,
        2, 1, 0,
        2, 3, 0,
        0, 0, 0,
    ] + list(map(ord, s)) + [0]

copy_buffer = [
    -4, 54, 3,
    54, 33, 6,
    54, 54, 9,
    -2, 54, 12,
    54, 30, 15,
    54, 31, 18,
    54, 37, 21,
    54, 54, 24,
    29, -3, 27,
    55, -3, -1,
    0, 0, 33,
    0, 54, 36,
    54, 0, 39,
    29, 30, 42,
    29, 31, 45,
    29, 37, 48,
    29, 33, 51,
    54, 54, 27,
    0, 1
]