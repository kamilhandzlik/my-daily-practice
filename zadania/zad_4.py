"""
Zadanie 4 - Django
1. Jak modele Book i Comic zostaną odwzorowane w bazie danych ?
2. Jakie zapytanie ORM pozwoli wypisać tytuły książek konkretnego wydawcy ?
3. Co jeśli chciałbym również wyprintować imiona autorów ?
"""
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(Publisher)


class Comic(models.Model):
    illustrator = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    hard_cover = models.BooleanField()

"""
Odpowiedzi:
1. Powstaną tabele Book i Comic, które będą miały następującą strukturę:
1.1 Nazwa tabeli = Book
    Nazwy kolumn/pól
    title - które jest polem ze znakami odpowienik string o maksymalnej ilości znaków 100
    author - "pole author to relacja wiele-do-jednego (ForeignKey), która przy usunięciu autora również usuwa książkę (przez on_delete=models.CASCADE)."
    publisher - relacyjne pole o właściwości wiele do wielu do Tabeli Publisher 

1.2 Nazwa tabeli = Comic
    illustrator - "pole illustrator to relacja wiele-do-jednego (ForeignKey), która przy usunięciu autora również usuwa komiks (przez on_delete=models.CASCADE)."
    pages - pole jako wartość przyjmujące tylko liczby całkowite.
    hard_cover - pole prawda fałsz albo ma twrdą okładkę albo nie.
2. Book.objects.filter(publisher__name="Nazwa Wydawcy").values_list("title", flat=True)
3. Book.objects.filter(publisher__name="Nazwa Wydawcy").select_related("autohr").values("title", "author_name")
"""