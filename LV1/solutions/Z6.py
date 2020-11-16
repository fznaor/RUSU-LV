# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:21:47 2020

@author: student
"""

emails = []
domains = dict()

filename = input('Ime datoteke: ')
try:
    file = open(filename)
    for line in file:
        if line.startswith('From: '):
             emails.append(line.split()[-1]) # odvoji dio linije nakon 'From: ', odnosno e-mail adresu
             domain = emails[-1].split('@')[-1] # odvoji dio e-mail adrese nakon znaka @ i spremi u dictionary
             if domain not in domains:
                 domains[domain] = 1
             else:
                 domains[domain] += 1
    print(emails[::5]) # ispis svake 5. e-mail adrese
    print(domains)
except FileNotFoundError:
    print('Odabrana datoteka ne postoji!')