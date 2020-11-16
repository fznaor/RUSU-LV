# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:58:00 2020

@author: Filip Znaor
"""

suma = 0
maxi = 0
mini = 0
n = 0

while True:
    try:
        unos = input('Unesite broj: ')
        if unos == 'Done':
            break
        broj = float(unos)
    except ValueError:
        print('Niste unijeli broj, pokusajte ponovno')
        continue
    if n == 0:
        maxi = broj
        mini = broj
    elif broj < mini:
        mini = broj
    elif broj > maxi:
        maxi = broj
    suma += broj
    n += 1
print('Broj unesenih brojeva: %d\nSrednja vrijednost: %.2f\nMaksimalna vrijednost: %.2f\nMinimalna vrijednost: %.2f' %(n, suma / n, maxi, mini))

