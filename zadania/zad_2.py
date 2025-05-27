"""
Zadanie 2 - Programowanie Obiektowe
1. Co zostanie wydrukowane w konsoli ?
2. Dlaczego tak się dzieje ?
3. Jaki nazywa się mechanizm, który jest za to odpowiedzialny ?
"""
class First(object):
    def check(self):
        print("First")

class Second(First):
    def check(self):
        print("Second")

class Third(First):
    def check(self):
        print("Third")

class Fourth(Third, Second):
    def check(self):
        super(Fourth, self).check()
        print("Fourth")


if __name__ == "__main__":
    Fourth().check()

"""
Odpowiedzi:
1. W konsoli zostanie wydrukowane: 
Third 
Fourth
2. Ponieważ klasa Fourth dziedziczy po Third i Second a metoda .super().check() odwołuje się
   do pierwszej metody check() znalezionej zgodnie z kolejnością MRO dla klasy Fourth z racji tego, że klasa Third jest
   jej pierwszym argumentem to w MRO pierwszą metodą check jest ta z klasy Third.
3. (Dziedziczenie, problem diamentu) W pythonie rozwiązane przez MRO czyli kolejność rozwiązywania metod dziedziczenie wielokrotne w Pythonie,
   w tym problem diamentu również odgrywają tu rolę ale głównym odpowiedzialnym tutaj jest MRO.
"""