from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from itertools import cycle

boston = load_boston()
x = boston.data
y = boston.target

print(boston.feature_names)

cycol = cycle('bgrcmk')

plt.figure()
plt.suptitle('Ovisnost cijene kuće o parametrima dataseta')

for i in range(6):
    plt.subplot(2, 3, i+1)
    if(i==3):
        plt.scatter(np.where(x[:, i]==0), y[x[:, i]==0], c='r', label='Nije uz rijeku')
        plt.scatter(np.where(x[:, i]==1), y[x[:, i]==1], c='g', label='Uz rijeku')
        plt.legend()
    elif i in [1,2,4]:
        plt.scatter(range(len(y)), y, c = x[:, i], cmap = 'inferno')
        plt.colorbar().set_label(boston.feature_names[i])
        plt.xlabel('Indeks')
    else:
        plt.scatter(x[:,i], y, c=next(cycol))
        plt.xlabel(boston.feature_names[i])
    plt.ylabel('Cijena kuće')

plt.figure() 
plt.suptitle('Ovisnost cijene kuće o parametrima dataseta')
   
for i in range(6, 12):
    plt.subplot(2, 3, i+1-6)
    if i in [8,9,10]:
        plt.scatter(range(len(y)), y, c = x[:, i], cmap = 'inferno')
        plt.colorbar().set_label(boston.feature_names[i])
        plt.xlabel('Indeks')
    else:
        plt.scatter(x[:,i], y, c=next(cycol))
        plt.xlabel(boston.feature_names[i])
    plt.ylabel('Cijena kuće')
        
plt.figure()
plt.hist(y, bins=10)
plt.title('Distribucija cijena kuća')
plt.xlabel('Vrijednost kuće u tisućama $')

lambdas = range(1000, 100001, 1000)

#pronalazak optimalnog stupnja polinoma i regularizacijskog parametra
for i in range(1, 6):
    MSE_train = []
    MSE_test = []

    poly = PolynomialFeatures(degree=i)
    x_t = poly.fit_transform(x)
    
    np.random.seed(12)
    indeksi = np.random.permutation(len(x_t))
    indeksi_train = indeksi[0:int(np.floor(0.7*len(x_t)))]
    indeksi_test = indeksi[int(np.floor(0.7*len(x_t)))+1:len(x_t)] 
    
    xtrain = x_t[indeksi_train]
    ytrain = y[indeksi_train]
    
    xtest = x_t[indeksi_test]
    ytest = y[indeksi_test] 
    
    for lmbd in lambdas:
        linearModel = lm.Ridge(lmbd)
        linearModel.fit(xtrain,ytrain)
        
        ytrain_p = linearModel.predict(xtrain)
        MSE_train.append(mean_squared_error(ytrain, ytrain_p))
    
        ytest_p = linearModel.predict(xtest)
        MSE_test.append(mean_squared_error(ytest, ytest_p))

    plt.figure()
    plt.xlabel('Regularizacijski parametar')
    plt.ylabel('Srednja kvadratna pogreška')
    plt.plot(lambdas, MSE_train, label = 'Train')
    plt.plot(lambdas, MSE_test, label = 'Test')
    plt.title('Vrijednosti pogrešaka za stupanj polinoma ' + str(i))
    plt.legend()

#treniranje i prikaz rezultata za stupanj polinoma 2 i vrijednost regularizacijskog parametra 3000
poly = PolynomialFeatures(degree=2)
x_t = poly.fit_transform(x)

np.random.seed(12)
indeksi = np.random.permutation(len(x_t))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x_t)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x_t)))+1:len(x_t)] 

xtrain = x_t[indeksi_train]
ytrain = y[indeksi_train]

xtest = x_t[indeksi_test]
ytest = y[indeksi_test] 

linearModel = lm.Ridge(3000)
linearModel.fit(xtrain,ytrain)

ytrain_p = linearModel.predict(xtrain)

ytest_p = linearModel.predict(xtest)
print('MSE = ' + str(mean_squared_error(ytest, ytest_p)))

plt.figure()
plt.ylim((0,60))
plt.scatter(range(len(ytest)), ytest[ytest.argsort()], c = 'g', label = 'Stvarna cijena')
plt.scatter(range(len(ytest)), ytest_p[ytest.argsort()], c = 'r', label = 'Predviđena cijena')
plt.vlines(range(len(ytest)), ytest[ytest.argsort()], ytest_p[ytest.argsort()])
plt.xlabel('Redni broj kuće')
plt.ylabel('Vrijednost kuće u tisućama $')
plt.legend()