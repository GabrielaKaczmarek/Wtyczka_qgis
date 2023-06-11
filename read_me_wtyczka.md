# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:13:24 2023

@author: Gabi
"""

READ ME - Projekt 2 Informatyka geodezyjna II

1) Do czego służy wtyczka?
Zadaniem wtyczki jest obliczenie przewyższenia pomiędzy dwoma punktami, a także pola powierzchni rozpartego pomiędzy minimum 3 punktami.

2) Na jakim systemie wtyczka została napisany oraz jakie są wymagania sprzętowe?
- System operacyjny Windows 10,
- 64 biotwy system operacyjny
- Python 3.9
- Qgis Białowieża 3.22

3) Inne wtyczki, które były niezbędne do utworzenia tej :
- Plugin Builder,
- Plugin Reloader,

4) Dane:
Dane powinny zostac zapisane w pliku o rozszerzeniu csv. Nalezy przedstawic je w jednostce metrycznej jaką jest metr oraz w 4 kolumnach rozdzielonych srednikami:  Nr ( Nr punktu), X, Y, Z. Jesli wartosc jest liczba zmienniprzecinkowa należy uzyc kropki, a nie przecinka.Plik powinien znalezc sie w tym samym folderze co wtyczka. 

Przykład pliku z danymi:
```sh
10001	5787483.773	7502302.207	114.319
10002	5787484.049	7500572.996	114.451
10003	5787486.154	7500524.107	114.548
10004	5786852.544	7500495.417	114.677
10005	5787408.780	7500499.203	114.459
```
5) Jak utworzyc warstwe z punktami, jesli nie mamy jej uprzednio przygotowanej?
Należy wykonac kolejno:
- menu - warstwa - dodaj warstwe - dodaj warstwe tekstowa CSV,
- Nazwa pliku - wybranie sciezki do pliku z danymi w rozszerzeniu csv,
- Nazwa warstwy - okreslic warstwe pod jakia utworzy nam sie warstwa z punktami,
- w oknie format pliku zaznaczyc opcje rozdzielone pod innym znakiem - srednik,
- w oknie Ustawinia geometrii  wybrac opcje wspolrzedne punktowe oraz w : Pole X, Pole Y zaznaczyc z rozwiniecia odpowiednio nazwy naszych kolumn z pliku csv, powinno to być X, Y.
- w tym samym oknie nalezy jeszcze ustawic uklad wspolrzednych, my opracowywalysmy wtyczke na ukladzie 1992,
- ostatnim etapem jest klikniecie przycisku dodaj, po którym utworzy nam sie warstwa punktowa.

6) Jak obsłużyć wtyczkę?
a) wgrać plik z danymi i utworzyć z nich warstwe w programie Qgis,
b) zaznaczyć porządane punkty do obliczen,
c) wybranie wtyczki,
d) wybranie, ktorej operacji matematycznej porządamy i kliknięcie 'Oblicz'
e) Wynik zostanie przedstawiony zaraz ponizej,
f) jesli wybrane punkty są nieprawidlowo dobrane zostaniesz o tym poinformowany.

7)Bledy
w przypadku wybrania nadprogramowej lub niewystarczającej ilości punków w zależnośći od powodu wyświetlą się następujące komunikaty:
Nadliczbowa liczba punktów 
 
lub 

Niewystarczająca ilosc punktów
