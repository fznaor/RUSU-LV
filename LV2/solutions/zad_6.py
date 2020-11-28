import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('../resources/tiger.png')
plt.imshow(img)

#svjetlija slika
img = img + 0.25 #povećavanje vrijednosti svih kanala slike za 0.25
plt.imshow(img)
