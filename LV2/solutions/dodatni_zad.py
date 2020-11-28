import matplotlib.pyplot as plt
import numpy as np

avgs = np.empty(1000, dtype = float)
stdevs = np.empty(1000, dtype = float)

for i in range(1000):
    throws = np.random.randint(1, 7, size = 30)
    avgs[i] = np.mean(throws)
    stdevs[i] = np.std(throws)
    
plt.hist(avgs, bins = 20) #razdioba srednjih vrijednosti, vidljivo je da poprima normalnu razdiobu
plt.xlabel('Srednja vrijednost')
plt.ylabel('Broj pojavljivanja')
print('Srednja vrijednost dobivene razdiobe je %.2f, a stand. devijacija %.2f.' %(np.mean(avgs), np.std(avgs)))


#ponavljanje 10000 puta
avgs = np.empty(10000, dtype = float)
stdevs = np.empty(10000, dtype = float)

for i in range(10000):
    throws = np.random.randint(1, 7, size = 30)
    avgs[i] = np.mean(throws)
    stdevs[i] = np.std(throws)

plt.figure(2)    
plt.hist(avgs, bins = 20) #povećavanjem broja izvođenja razdioba sve više liči na Gaussovu krivulju
plt.xlabel('Srednja vrijednost')
plt.ylabel('Broj pojavljivanja')
print('Srednja vrijednost dobivene razdiobe je %.2f, a stand. devijacija %.2f.' %(np.mean(avgs), np.std(avgs)))
