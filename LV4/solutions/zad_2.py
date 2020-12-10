import numpy as np

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

theta = np.linalg.inv(np.transpose(xtrain) @ xtrain) @ np.transpose(xtrain) @ ytrain
print(theta)