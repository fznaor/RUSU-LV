import numpy as np
import matplotlib.pyplot as plt

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y
 
def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

x = np.linspace(1,10,100)
y_true = non_func(x)
y_measured = add_noise(y_true)

np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]

x = x[:, np.newaxis]
x = np.append(np.ones((len(x), 1)), x, axis = 1)
y_measured = y_measured[:, np.newaxis] 

xtrain = x[indeksi_train]
ytrain = y_measured[indeksi_train]

theta = np.zeros((2,1))
alfas = [0.001, 0.01, 0.05, 0.08]

for alfa in alfas:
    criterias = []
    for itr in range(500):
        sume = np.zeros((1,2))
        for i in range(xtrain.shape[0]):
            sume += ((xtrain[i] @ theta - ytrain[i]) * xtrain[i])
        sume /= xtrain.shape[0]
        theta -= alfa * sume.transpose()
        criterias.append(1/(2*len(xtrain)) * np.sum((xtrain @ theta - ytrain) ** 2))
        
    print(criterias[0])
    print('Stopa učenja = %.2f' %alfa)
    print(theta)
    
    plt.plot(range(len(criterias)), criterias, label = 'alfa = ' + str(alfa))

plt.ylim((0.5, 1))
plt.xlabel('Iteracija')
plt.ylabel('Vrijednost kriterijske funkcije')
plt.legend()