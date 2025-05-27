"""
Zadanie 1: Analiza danych giełdowych
Opis: Masz dostęp do danych dziennych notowań akcji spółek z indeksu WIG20 za ostatnie 5 lat.

Zadania:

Wczytaj dane i sprawdź ich kompletność oraz poprawność.

Oblicz średnią dzienną stopę zwrotu dla każdej spółki.

Zidentyfikuj spółki o najwyższej i najniższej zmienności cenowej.

Przygotuj wykres porównujący stopy zwrotu wybranych spółek.

Wskazówki: Użyj bibliotek pandas, numpy i matplotlib.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Wczytaj dane i sprawdź ich kompletność oraz poprawność.
# 1.1 wczytanie danych
df = pd.read_csv("wig20_simulated_data.csv")
print(df.head())
# 1.2 Sprawdzenie brakujących danych
print(f"\nBrakujące wartości w kolumnach:\n\33[31m{df.isnull().sum()}\033[0m")
# 1.3 Sprawdzenie typu danych
print(f"\nBrakujące typu danych:\n\33[33m{df.dtypes}\033[0m")
# 1.4 Unikalne spółki
print(f"\nLiczba unikalnych spółek:\n\33[34m{df["Company"].unique()}\033[0m")
# 1.5 Zakres dat
print(f"\nZakres dat:\n\33[33m{df['Date'].min()} -> {df['Date'].max()}\033[0m")

# 2. Oblicz średnią dzienną stopę zwrotu dla każdej spółki.
returns = (
    df.sort_values(["Company", "Date"]).groupby("Company")["Close_Price"].apply(lambda x: x.pct_change().mean())
)
print(f"\nŚrednia dzienna stopa zwrotu dla każdej spółki:\n{returns.sort_values(ascending=False)}")

# 3. Zidentyfikuj spółki o najwyższej i najniższej zmienności cenowej.
# 3.1 Dzienne stopy zwrotu
df_sorted = df.sort_values(by=["Company", "Date"])
df_sorted["Return"] = df_sorted.groupby("Company")["Close_Price"].pct_change()
# 3.2 zmienność
volatility = df_sorted.groupby("Company")["Return"].std()
most_volatile = volatility.sort_values(ascending=False).head(3)
least_volatile = volatility.sort_values().head(3)
print(f"\n\033[31m3 najbardziej zmienne spółki:{most_volatile}\033[0m\n")
print(f"\n\033[32m3 najmniej zmienna spółki: {least_volatile}\033[0m\n")

# 4. Przygotuj wykres porównujący stopy zwrotu wybranych spółek.
top_returns = returns.sort_values(ascending=False).head(5)
botton_returns = returns.sort_values().head(5)

selected_return = pd.concat([top_returns, botton_returns])

plt.figure(figsize=(12, 6))
selected_return.plot(kind="bar", color="skyblue")
plt.title("Średnie dzienne stopy zwrotu wybranych spółek")
plt.ylabel("Średnia stopa zwrotu")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
