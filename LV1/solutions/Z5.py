# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:08:24 2020

@author: Filip Znaor
"""

suma = 0
count = 0

filename = input('Ime datoteke: ')
file = open(filename)
for line in file:
    if line.startswith('X-DSPAM-Confidence: '):
        count += 1
        suma += float(line.split()[-1])
print('Average X-DSPAM-Confidence: ', suma / count)

