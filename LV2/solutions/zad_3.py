import numpy as np
import matplotlib.pyplot as plt

spol = np.random.randint(2, size = 100)
visine = np.zeros(100, dtype = int)
visine[spol == 1] = np.random.normal(180, 7, len(visine[spol == 1])) #generiranje visina muškaraca
visine[spol == 0] = np.random.normal(167, 7, len(visine[spol == 0])) #generiranje visina žena

plt.scatter(np.where(spol == 0), visine[spol == 0], c = 'r') #iscrtavanje žena
plt.scatter(np.where(spol == 1), visine[spol == 1], c = 'b') #iscrtavanje muškaraca
plt.axhline(y = np.mean(visine[spol == 0]), c = 'red', ls = ':') #prosječna visina žena
plt.axhline(y = np.mean(visine[spol == 1]), c = 'blue', ls = ':') #prosječna visina muškaraca
plt.title('Visine ljudi')
plt.xlabel('Redni broj')
plt.ylabel('Visina [cm]')
plt.legend(['Prosječna visina žena','Prosječna visina muškaraca','Žena','Muškarac'])