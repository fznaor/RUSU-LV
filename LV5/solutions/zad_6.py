import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

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

def getDistanceMatrix(x,y):
    distances = np.empty((x.shape[0], y.shape[0]))
    for i in range(y.shape[0]):
        for j in range(x.shape[0]):
            distances[j,i] = np.sqrt(np.sum((y[i,:] - x[j,:])**2))
    return distances

def kMeans(X, n_clusters):
    centers = X[np.random.choice(X.shape[0], size=n_clusters, replace=False)]
    centers_list = [centers.copy()]
    labels = np.empty(X.shape[0], dtype=int)
    
    for iteration in range(100):
        distances = getDistanceMatrix(X, centers)
        for i in range(labels.shape[0]):
            labels[i] = np.argmin(distances[i,:])
        for i in range(n_clusters):
            centers[i] = np.mean(X[labels==i], axis=0)
        centers_list.append(centers.copy())
    return labels, centers_list

cluster_counts = [3, 3, 4, 2, 2]

for i in range(5):      
    X = generate_data(500, i+1)
    labels, centers = kMeans(X, cluster_counts[i])
    
    plt.figure()
    plt.scatter(X[:,0], X[:,1], c = labels)
    
    for center in centers:
        plt.scatter(center[:,0], center[:,1], c = 'r', marker = '*')
        
    for j in range(len(centers) - 1):
        for k in range(cluster_counts[i]):
            plt.plot([centers[j][k][0], centers[j+1][k][0]], [centers[j][k][1], centers[j+1][k][1]], c = 'k')