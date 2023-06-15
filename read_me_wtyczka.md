# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:13:24 2023

@author: Gabi
"""

# Wtyczka do programu Qgis
Wtyczka służy do :
1   -  obliczania przewyższeń między 2 punktami 
2   -  obliczanaia pola powierzchni dla minimum 3 punktów używając metody Gaussa.

## wymagania sprzętowe :
- Windows 10  
- Qgis: 3.22.16

## Jak działa wtyczka :
wspolrzędne punktów pobierane są z qgis z geometrii punktów

1. Użytkownik wybiera 2 lub 3/4 punkty odpowiednio dla obliczenia przewyższenia lub pola powierzchni.
2. Następnie otwiera wtyczkę i klika przycisk odpowiedni dla danego działania.

Po wybraniu odpowiednije iloci punktow w zaleznosci od oczekiwanych rezultatów nalezy uruchomic wtyczke.
Następnie nalezy obliczenia zostają uruchomione po wcisnięciu odpowiedniego przycisku:
```sh
Oblicz
```
przy opcji :
1 - Uzyskane przewyzszenie
2 - Uzyskane pole powierzchni

3. Wynik jest wyświetlany pod danym przyciskiem.

## Możliwe błedy :
w przypadku wybrania niewystarczającej ilości punków wyświetli się następujący komunikat:

```sh
Niewystarczająca ilosc punktów
```
