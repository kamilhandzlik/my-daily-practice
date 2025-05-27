"""
Zadanie 3 - Asynchroniczność
1. Co zostanie wydrukowane w konsoli ?
2. Dlaczego tak się dzieje ?
3. Po co wogóle używać kodu asynchronicznego ?
"""

import asyncio

async def fetchdata(delay, data):
    print(f"Fetching {data}...")
    await asyncio.sleep(delay)
    print(f"Fetched {data}...")
    return data

async def main():
    tasks = [
        fetchdata(delay=2, data="data1"),
        fetchdata(delay=3, data="data2"),
        fetchdata(delay=1, data="data3"),
    ]

    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
"""
Odpowiedzi:
1. W konsoli wydrukowane zostanie:
   Fetching data1...
   Fetching data2...
   Fetching data3...
   Fetched data3
   Fetched data1
   Fetched data2
   Results: ['data1', 'data2', 'data3']
2. Wywołanie asyncio.gather(*tasks) uruchamia wszystkie zadania równolegle (asynchronicznie), dlatego wszystkie trzy linijki
  Fetching... pojawiają się niemal natychmiast po sobie – jedno po drugim, zanim await asyncio.sleep(delay) przejmie kontrolę.

Następnie, ponieważ każde zadanie ma inny czas opóźnienia (delay), linijki Fetched... pojawiają się zgodnie z upływem czasu:

Fetched data3... po 1 sekundzie,

Fetched data1... po 2 sekundach,

Fetched data2... po 3 sekundach.

   Ale mimo że Fetched wypisuje się w kolejności czasowej, wynik results (['data1', 'data2', 'data3']) ma taką samą kolejność,
   jakiej użyliśmy w liście tasks. To dlatego, że asyncio.gather() dba o zachowanie kolejności wyników zgodnie z kolejnością zadań,
   nawet jeśli zakończyły się w innej kolejności.
3. Po co w ogóle używać kodu asynchronicznego?
   Kod asynchroniczny pozwala wykonywać inne operacje (np. kolejne zadania) w czasie, gdy jakieś
    zadanie czeka – np. na dane z sieci, na plik z dysku lub na sen (sleep). Dzięki temu nasz program nie „marnuje czasu” 
    czekanie, tylko może w międzyczasie robić inne rzeczy. Idealne, gdy mamy wiele operacji I/O, np. pobieranie danych z API, serwera, czy przetwarzanie strumieni.



Ważne!!! Trzeba pamiętać, że  GIL (czyli Global Interpreter Lock) w CPythonie rzuca cień na prawdziwą współbieżność wątków,
 ALE — i tu pojawia się klasyczna „gwiazdka jak w reklamie proszku do prania” — nie dotyczy to asynchroniczności jako takiej.
GIL – co to za potwór?
GIL to mechanizm w interpreterze CPython, który ogranicza wykonywanie kodu Pythona do jednego wątku naraz, nawet na procesorze wielordzeniowym.
 Takie zabezpieczenie ułatwia zarządzanie pamięcią, ale blokuje prawdziwą równoległość w wątkach dla kodu CPU-heavy.

⚙️ Ale… asyncio to nie są wątki!
Dokładnie! asyncio i inne asynchroniczne podejścia (np. await, async def) nie tworzą nowych wątków ani procesów – one działają
na pojedynczym wątku, który przełącza kontekst między zadaniami (korutynami), gdy tylko napotka operację, która może czekać (np. await asyncio.sleep(), await response.json() itp.).

To trochę jak stary skryba, który prowadzi kilka listów naraz – gdy czeka, aż atrament na jednym wyschnie, pisze kolejny.
Rodzaj operacji	Czy GIL przeszkadza?	Wyjaśnienie
Asynchroniczność (asyncio)	❌ Nie	Działa w pojedynczym wątku, przełączając się między zadaniami
Wielowątkowość (threading)	✅ Tak	Tylko jeden wątek może wykonywać kod Pythona na raz
Wieloprocesowość (multiprocessing)	❌ Nie	Każdy proces ma własny GIL, więc działa równolegle
Operacje I/O (np. pobieranie danych)	✅/❌ Nie zawsze przeszkadza	Asynchroniczne I/O działa dobrze, GIL nie blokuje sleep, read, wait
"""