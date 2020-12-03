import pandas as pd

cars = pd.read_csv('../resources/mtcars.csv')

#5 automobila s najvećom potrošnjom
print(cars.sort_values(['mpg'], ascending = False).head(5)[['car', 'mpg']])

#3 automobila s 8 cilindara i najmanjom potrošnjom
print(cars[cars.cyl == 8].sort_values(['mpg']).head(3)[['car', 'mpg', 'cyl']])

print('Srednja potrošnja automobila sa 6 cilindara iznosi %.2f mpg.' %cars[cars.cyl == 6].mpg.mean())

print('Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs iznosi %.2f mpg' %cars[(cars.cyl == 4) & (cars.wt >= 2) & (cars.wt <= 2.2)].mpg.mean())

print('U skupu je %d automobila s ručnim i %d auta s automatskim mjenjačem.' %(len(cars[cars.am == 1]), len(cars[cars.am == 0])))

print('U skupu je %d automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga.' %len(cars[(cars.am == 0) & (cars.hp > 100)]))

#masa automobila u kg
cars['kg'] = cars.wt * 453.592
print(cars[['car', 'kg']])