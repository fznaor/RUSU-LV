import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('../resources/mtcars.csv')

plt.scatter(cars.hp, cars.mpg, c = cars.wt * 1000, cmap = 'inferno')
plt.colorbar().set_label('Masa [lbs]')
plt.xlabel('Konjske snage')
plt.ylabel('Potrošnja [mpg]')

print('Minimalna vrijednost potrošnje: %.2f mpg' %cars.mpg.min())
print('Maksimalna vrijednost potrošnje: %.2f mpg' %cars.mpg.max())
print('Prosječna vrijednost potrošnje: %.2f mpg' %cars.mpg.mean())