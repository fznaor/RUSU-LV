import numpy as np
import matplotlib.pyplot as plt

def prosjecna_visina(n):
    if n == 1:
        return np.dot(visine, spol) / np.count_nonzero(spol == 1) #muškarci
    elif n == 0:
        return -np.dot(visine, spol - 1) / np.count_nonzero(spol == 0) #žene
    else:
        return 0

spol = np.random.randint(2, size = 100)
visine = np.zeros(100, dtype = int)
visine[spol == 1] = np.random.normal(180, 7, len(visine[spol == 1])) #generiranje visina muškaraca
visine[spol == 0] = np.random.normal(167, 7, len(visine[spol == 0])) #generiranje visina žena

plt.scatter(np.where(spol == 0), visine[spol == 0], c = 'r') #iscrtavanje žena
plt.scatter(np.where(spol == 1), visine[spol == 1], c = 'b') #iscrtavanje muškaraca
plt.axhline(y = prosjecna_visina(0), c = 'red', ls = ':') #prosječna visina žena
plt.axhline(y = prosjecna_visina(1), c = 'blue', ls = ':') #prosječna visina muškaraca
plt.title('Visine ljudi')
plt.xlabel('Redni broj')
plt.ylabel('Visina [cm]')
plt.legend(['Prosječna visina žena','Prosječna visina muškaraca','Žena','Muškarac'])

