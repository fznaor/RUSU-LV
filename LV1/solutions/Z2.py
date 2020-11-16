# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:45:13 2020

@author: Filip Znaor
"""

import sys

try:
    broj = float(input('Unesite broj izmedju 0.0 i 1.0: '))
except ValueError:
    print('Niste unijeli broj!')
    sys.exit()
if broj > 1 or broj < 0:
    print('Niste unijeli broj izmedju 0.0 i 1.0!')
elif broj >= 0.9:
    print('A')
elif broj >= 0.8:
    print('B')
elif broj >= 0.7:
    print('C')
elif broj >= 0.6:
    print('D')
else:
    print('F')