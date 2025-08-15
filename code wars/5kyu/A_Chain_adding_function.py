"""
We want to create a function that will add numbers together when called in succession.

add(1)(2) # equals 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3) # 6
add(1)(2)(3)(4); # 10
add(1)(2)(3)(4)(5) # 15
and so on.

A single call should be equal to the number passed in.

add(1) # 1
We should be able to store the returned values and reuse them.

addTwo = add(2)
addTwo # 2
addTwo + 5 # 7
addTwo(3) # 5
addTwo(3)(5) # 10
We can assume any number being passed in will be valid whole number.
"""

# Solution 1
class Add:
    """Obiekt sumujący, który:
    - pozwala na łańcuchowe wywołania: add(1)(2)(3) -> 6
    - zachowuje się jak liczba (można go dodać do int, wypisać itd.)
    """
    __slots__ = ("_total",)

    def __init__(self, total=0):
        self._total = int(total)

    # Umożliwia kolejne wywołania: add(1)(2) -> Add(3)
    def __call__(self, n=None):
        if n is None:
            return self
        return Add(self._total + int(n))

    # Dzięki temu obiekt „wygląda” jak liczba przy wypisywaniu
    def __repr__(self):
        return str(self._total)

    __str__ = __repr__

    # Konwersje numeryczne
    def __int__(self):
        return self._total

    def __float__(self):
        return float(self._total)

    # Działania arytmetyczne z liczbami i z innym Add
    def _to_num(self, other):
        return other._total if isinstance(other, Add) else int(other)

    def __add__(self, other):
        return self._total + self._to_num(other)

    def __radd__(self, other):
        return self._to_num(other) + self._total

    # (opcjonalnie) porównania z liczbami
    def __eq__(self, other):
        try:
            return self._total == self._to_num(other)
        except Exception:
            return False


def add(n):
    """Punkt wejścia zgodny z treścią zadania: add(1)(2) ..."""
    return Add(n)


# Solution 2
class Add:
    def __init__(self, total):
        self.total = total

    def __call__(self, n=None):
        if n is None:
            return self
        return Add(self.total + n)

    def __int__(self):
        return self.total

    def __add__(self, other):
        return self.total + int(other)

    __radd__ = __add__

    def __eq__(self, other):
        return self.total == int(other)

    def __repr__(self):
        return str(self.total)


def add(n):
    return Add(n)


# Solution 3
class add(int):
    def __call__(self,n):
        return add(self+n)