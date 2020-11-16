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
             emails.append(line.split()[-1])
             domain = emails[-1].split('@')[-1]
             if domain not in domains:
                 domains[domain] = 1
             else:
                 domains[domain] += 1
    print(emails[::5])
    print(domains)
except FileNotFoundError:
    print('Odabrana datoteka ne postoji!')