import matplotlib.pyplot as plt
import numpy as np

throws = np.random.randint(1, 7, size = 100)
plt.hist(throws, bins = 20)
plt.xlabel('Vrijednost')
plt.ylabel('Broj pojavljivanja')
