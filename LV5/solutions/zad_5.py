from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imageNew = mpimg.imread('../resources/example.png')
    
X = imageNew.reshape((-1, 1))

plt.figure()
plt.title('Originalna slika')
plt.imshow(imageNew,  cmap='gray')

for clusterCount in range(2, 11):
    k_means = cluster.KMeans(n_clusters=clusterCount, n_init=1)
    k_means.fit(X) 
    values = k_means.cluster_centers_.squeeze()
    labels = k_means.labels_
    imageNew_compressed = np.choose(labels, values)
    imageNew_compressed.shape = imageNew.shape
    
    
    plt.figure()
    plt.title('Slika komprimirana u %d clustera' %clusterCount)
    plt.imshow(imageNew_compressed,  cmap='gray')