import re

email_names = []

file = open('../resources/mbox-short.txt')

for line in file:
    emails = re.findall('[a-z0-9]+[\._]?[a-z0-9]+[@]\w+', line)
    print(emails)
    for email in emails:
        email_names.append(email.split('@')[0])
    
print(email_names)