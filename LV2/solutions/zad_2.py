import re

email_names = []

file = open('../resources/mbox-short.txt')

for line in file:
    emails = re.findall('[a-z0-9]+[\._]?[a-z0-9]+[@]\w+', line)
    for email in emails:
        email_names.append(email.split('@')[0])

#najmanje jedno slovo a
r = re.compile('\S*a\S*')
zad_1 = list(filter(r.match, email_names)) #upotreba kompajliranog regexa na cijeloj listi i spremanje rezultata u novu listu
print(zad_1)

#točno jedno slovo a
r = re.compile('^[^a]*a[^a]*$')
zad_2 = list(filter(r.match, email_names))
print(zad_2)

#ne sadrži a
r = re.compile('^[^a]+$')
zad_3 = list(filter(r.match, email_names))
print(zad_3)

#sadrži jedan ili više numeričkih znakova
r = re.compile('\S*[0-9]\S*')
zad_4 = list(filter(r.match, email_names))
print(zad_4)

#sadrži samo mala slova
r = re.compile('^[a-z]+$')
zad_5 = list(filter(r.match, email_names))
print(zad_5)