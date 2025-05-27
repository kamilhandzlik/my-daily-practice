"""
Zadanie 1 - Python
1. Co zostanie wydrukowane w konsoli ?
2. Co jeśli chciałbym wyprintować print(a)
3. Co jeśli chciałbym aby listy a i b były oddzielnymi obiektami ?
"""
# import copy

a = [1, 2, 3, 4]
b = a
# b = copy.copy(a)

b.append(5)

if __name__ == "__main__":
    print(b)
    print(a)

"""
Odpowiedzi:
1. W terminalu pojawi się [1, 2, 3, 4, 5].
2. W terminalu pojawi się [1, 2, 3, 4, 5].
3. Zamiast b = a trzeba by było zaimportować copy a następnie użyć b = copy.copy(a)
"""