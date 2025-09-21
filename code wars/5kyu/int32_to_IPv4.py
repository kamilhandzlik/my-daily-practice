"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

Examples
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"
"""

# Version 1
def int32_to_ip(int32):
    binary = f"{int32:032b}"
    first = int(binary[:8], 2)
    second = int(binary[8:16], 2)
    third = int(binary[16:24], 2)
    fourth = int(binary[24:32], 2)
    return f"{first}.{second}.{third}.{fourth}"

# Version 2
def int32_to_ip(int32):
    binary = f"{int32:032b}"
    return f"{int(binary[:8], 2)}.{int(binary[8:16], 2)}.{int(binary[16:24], 2)}.{int(binary[24:32], 2)}"

# Version 3
def int32_to_ip(int32: int) -> str:
    binary = f"{int32:032b}"

    octets = [
        str(int(binary[i:i + 8], 2))
        for i in range(0, 32, 8)
    ]

    return ".".join(octets)

print(int32_to_ip(2154959208))
print(int32_to_ip(0))