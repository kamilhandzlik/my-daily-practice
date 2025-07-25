"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


def clamp(x):
    return max(0, min(x, 255))


def rgb(r, g, b):
    return "{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b)).upper()


# or

def rgb(r, g, b):
    return f"{clamp(r):02X}{clamp(g):02X}{clamp(b):02X}"


"""
Tu mamy do czynienia z formatowaniem liczb całkowitych jako szesnastkowe (hex) ciągi znaków – jak w kodzie koloru HTML (#ff00ff, itp.).

:02x oznacza:

0 – wypełnienie zerami, jeśli liczba jest jednocyfrowa,

2 – zawsze dwa znaki,

x – formatowanie jako hex z małych liter (używając X zamiast x miałbyś wielkie litery).
"""