from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster as clstr

def generate_data(n_samples, flagc):

    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
    
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
    
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples, centers = 4,
        cluster_std=[1.0, 2.5, 0.5, 3.0],
        random_state=random_state)
    
    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
    
    return X

for i in range(1,6):
    X = generate_data(500, i)
    inertias = []
    
    for clusters in range(2,21):
        kmeans = clstr.KMeans(clusters).fit(X)
        inertias.append(kmeans.inertia_)
    
    plt.figure(i)
    plt.title('Vrijednost i kriterijske funkcije za skup podataka %d' %i)
    plt.xlabel('Broj clustera')
    plt.ylabel('Kriterijska funkcija')
    plt.plot(range(2,21), inertias)