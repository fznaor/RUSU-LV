# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:54:42 2020

@author: Filip Znaor
"""

def total_kn(sati, cijena):
    return sati * cijena

sati = float(input('Unesite broj radnih sati: '))
cijena = float(input('Unesite zaradu po satu u kunama: '))
print('Ukupno: %.2f kn' %total_kn(sati, cijena))
