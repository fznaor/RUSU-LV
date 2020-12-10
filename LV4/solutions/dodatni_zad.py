import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

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

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis] 

poly = PolynomialFeatures(15)
xnew = poly.fit_transform(x) 

np.random.seed(12)
indeksi = np.random.permutation(len(xnew))
indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew)))]
indeksi_test = indeksi[int(np.floor(0.7*len(xnew)))+1:len(xnew)] 

xtrain = xnew[indeksi_train,]
ytrain = y_measured[indeksi_train]

xtest = xnew[indeksi_test,]
ytest = y_measured[indeksi_test]

MSEtrain = []
MSEtest = []
lambdas = [0.001, 0.01, 0.1, 0.2]
labels = ['Lambda = 0.001', 'Lambda = 0.01', 'Lambda = 0.1', 'Lambda = 0.2']
styles = ['r-', 'b-', 'y-', 'g-']

plt.figure(5)
plt.plot(x,y_true,label='f')
plt.xlabel('x')
plt.ylabel('y')

for i in range(4):
    linearModel = lm.Lasso(lambdas[i], max_iter = 10000000)
    linearModel.fit(xtrain,ytrain)
    
    ytest_p = linearModel.predict(xtest)
    ytrain_p = linearModel.predict(xtrain)
    MSEtest.append(mean_squared_error(ytest, ytest_p))
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    
    plt.plot(x, linearModel.predict(xnew),styles[i],label=labels[i])

plt.plot(xtrain[:,1],ytrain,'ok',label='train')
plt.legend(loc = 4) 

print(MSEtrain)
print(MSEtest)