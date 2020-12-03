import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('../resources/mtcars.csv')

cars.groupby(cars.cyl).mpg.mean().plot.bar()
plt.xlabel('Broj cilindara')
plt.ylabel('Prosječna potrošnja [mpg]')

cars.boxplot(column = 'wt', by = ['cyl'])
plt.xlabel('Broj cilindara')
plt.ylabel('Masa [lb/1000]')
plt.title("")
plt.suptitle("")

cars.boxplot(column = 'mpg', by = ['am']) #auti s ručnim mjenjačem imaju veću potrošnju
plt.xticks([1, 2], ['Automatski', 'Ručni'])
plt.xlabel('Vrsta mjenjača')
plt.ylabel('Potrošnja [mpg]')
plt.title("")
plt.suptitle("")


plt.figure(4)
plt.scatter(cars[cars.am == 0].hp, cars[cars.am == 0].qsec, label = 'Automatski')
plt.scatter(cars[cars.am == 1].hp, cars[cars.am == 1].qsec, label = 'Ručni')
plt.xlabel('Konjske snage')
plt.ylabel('Ubrzanje [1/4 mile time]')
plt.legend()