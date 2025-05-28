"""
 Zadanie 2: Analiza sektorowa spółek giełdowych
Opis:
Masz dostęp do danych dziennych notowań akcji spółek z trzech różnych sektorów (np. bankowość, energetyka, technologia) notowanych na GPW, z lat 2019–2024. Twoim zadaniem jest przeprowadzenie analizy porównawczej tych sektorów.

🎯 Zadania:
Wczytaj dane z pliku CSV i sprawdź kompletność danych (czy są braki, błędy, duplikaty).

Oblicz średnią miesięczną stopę zwrotu dla każdej spółki i każdej branży.

Zidentyfikuj sektor o największym wzroście i największym spadku w ujęciu rocznym.

Porównaj średnią zmienność dzienną (odchylenie standardowe stóp zwrotu) w sektorach.

Wygeneruj wykresy:

wykres pudełkowy (boxplot) stóp zwrotu dla każdego sektora,

liniowy wykres zmian indeksu sektorowego (średnia cen spółek sektora w czasie).
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# 1. Wczytaj dane z pliku CSV i sprawdź kompletność danych (czy są braki, błędy, duplikaty).
df = pd.read_csv("dane_spolek.csv")
print(df.head())
# 1.1 Sprawdzenie brakujących danych
print(f"\n\33[31mSprawdzenie brakujących danych: {df.isnull().sum()}\33[0m")
# 1.2 Sprawdzenie błędów
print("\n\033[31mSprawdzenie błędów logicznych:\033[0m")
print("Czy są wiersze, gdzie low > high?")
print(df[df['low'] > df['high']])
print("\nCzy są ujemne wartości wolumenu?")
print(df[df["volume"] < 0])
# 1.3 Sprawdzenie duplikatów
print(f"\n\33[31mSprawdzenie duplikatów: {df.duplicated()}\33[0m")
# 1.4 Sprawdzenie typu danych
print(f"\n\33[32mSprawdzenie typu danych: {df.dtypes}\33[0m")

# 2. Oblicz średnią miesięczną stopę zwrotu dla każdej spółki i każdej branży.
df['date'] = pd.to_datetime(df['date'])
df['daily_return'] = df.groupby('symbol')['close'].pct_change()
df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
monthly_avg_returns = df.groupby(['symbol', 'month'])['daily_return'].mean().reset_index()
print("\n\033[32mŚrednie miesięczne stopy zwrotu:\033[0m")
print(monthly_avg_returns.head())

# Zidentyfikuj sektor o największym wzroście i największym spadku w ujęciu rocznym.
# Roczne maksima i minima
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.to_period("Y").dt.to_timestamp()
yearly_rises = df.groupby(["sector", "year"])['high'].mean().reset_index()
yearly_drops = df.groupby(["sector", "year"])['low'].mean().reset_index()
print(f"\n\033[32mŚrednie roczne wzrosty:\n{yearly_rises}\033[0m")
print(f"\n\033[31mŚrednie roczne spadki:\n{yearly_drops}\033[0m")

# Obliczamy średnią cenę zamknięcia (lub używamy ceny z początku i końca roku)
df['year'] = df['date'].dt.year
annual_returns = df.groupby(['sector', 'year'])['close'].mean().pct_change().dropna().reset_index()

# albo bardziej precyzyjnie: używając tylko początku i końca roku
first_last = df.sort_values(['sector', 'date']).groupby(['sector', 'year'])['close'].agg(['first', 'last']).reset_index()
first_last['yearly_return'] = (first_last['last'] - first_last['first']) / first_last['first']

print("\n\033[34mRoczna stopa zwrotu dla każdego sektora:\033[0m")
print(first_last[['sector', 'year', 'yearly_return']])

# Porównaj średnią zmienność dzienną (odchylenie standardowe stóp zwrotu) w sektorach.
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# Obliczamy odchylenie standardowe stóp zwrotu w sektorach
sector_volatility = df.groupby('sector')['daily_return'].std().sort_values(ascending=False)

print("\n\033[36mŚrednia zmienność dzienna (odchylenie standardowe stóp zwrotu) w sektorach:\033[0m")
print(sector_volatility)
# Wygeneruj wykresy:
# wykres pudełkowy (boxplot) stóp zwrotu dla każdego sektora,
# liniowy wykres zmian indeksu sektorowego (średnia cen spółek sektora w czasie).

import matplotlib.pyplot as plt

# Filtrujemy dane, usuwamy NaN-y (bo są po pct_change)
df_filtered = df[['sector', 'daily_return']].dropna()

# Grupujemy dane do boxplotu
sectors = df_filtered['sector'].unique()
data_to_plot = [df_filtered[df_filtered['sector'] == sector]['daily_return'] for sector in sectors]

# Tworzymy wykres
plt.figure(figsize=(12, 6))
plt.boxplot(data_to_plot, labels=sectors, patch_artist=True, medianprops=dict(color='black'))
plt.xticks(rotation=45)
plt.title("Rozkład stóp zwrotu w sektorach (Boxplot)")
plt.ylabel("Dzienna stopa zwrotu")
plt.xlabel("Sektor")
plt.grid(axis='y')
plt.tight_layout()
plt.show()