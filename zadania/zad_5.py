"""
Zadanie 5 - Algorytmika
Napisz funkcję która przyjmuje 3 parametry. Funkcja ma za zadanie sprawdzić, czy z podanych parametrów można stworzyć trójkąt. Funkcja zwraca True jeśli da się stworzyć trójkąt, False, jeśli się nie da.
"""


def check_if_triangle(a, b, c):
    return False if a >= b + c or b >= a + c or c >= a + b else True

print(check_if_triangle(1, 2, 3))
print(check_if_triangle(6, 3, 2))
print(check_if_triangle(4, 6, 4))
print(check_if_triangle(6, 6, 6))
