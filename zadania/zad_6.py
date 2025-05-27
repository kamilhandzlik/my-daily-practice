"""
Zadanie 6 - SQL
1. Napisz zapytanie SQL, które wyciagnie duplikaty (autorzy o takim samym imieniu)
2. Co jeśli chciałbym to zrobić uzywając Django ORM?
3. Jakie są zalety i wady używania ORM, w porównaniu z czystym SQL ?
"""

from django.db import models
from django.db.models import  Count

class Author(models.Model):
    name = models.CharField(max_length=100)



# SELECT email, COUNT(*)
# FROM employees
# GROUP BY email
# HAVING COUNT(*) > 1;
#
duplicates = Author.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

"""
Odpowiedzi:
1. Zakładamy, że interesują nas autorzy z tym samym imieniem (czyli kolumną name). Poprawne zapytanie SQL to:
SELECT name, COUNT(*) as count
FROM Author
GROUP BY name
HAVING COUNT(*) > 1;
To klasyczna szkoła SQL – grupujemy po kolumnie name i wybieramy tylko te grupy, w których imię powtarza się więcej niż raz.

2. Najpierw trzeba zaimportować Count z Django ORM:


from django.db.models import Count
A potem zapytanie wygląda tak:


duplicates = Author.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)
To zapytanie:

values('name') – grupuje po imieniu,

annotate(Count('name')) – zlicza, ile razy imię występuje,

filter(name_count__gt=1) – wyciąga tylko te, które występują więcej niż raz.

3. Jakie są zalety i wady używania ORM, w porównaniu z czystym SQL?
Zalety ORM	                                                            Wady ORM
✅ Czytelność i łatwość użycia – przypomina kod w Pythonie, a nie SQL	❌ Mniejsza wydajność przy skomplikowanych zapytaniach
✅ Odporność na błędy składni SQL	                                    ❌ Czasem generuje nieoptymalne zapytania
✅ Integracja z modelem aplikacji – dane są zwracane jako obiekty	    ❌ Mniej kontroli nad złożoną logiką biznesową
✅ Łatwe do testowania i refaktoryzacji	                                ❌ ORM nie obsłuży wszystkich konstrukcji SQL (np. WITH RECURSIVE)
✅ Przenośność między bazami danych	                                    ❌ Trudniej debugować w przypadku problemów z wydajnością


"""