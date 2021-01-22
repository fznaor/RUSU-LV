import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def add_noise(y):
	
	np.random.seed(14)
	varNoise = np.max(y) - np.min(y)
	y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
	return y_noisy


def non_func(n):
	
	x = np.linspace(1,10,n)
	y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
	y_measured = add_noise(y)
	data = np.concatenate((x,y,y_measured),axis = 0)
	data = data.reshape(3,n)
	return data.T

# kreiranje podataka
np.random.seed(242)
X_train = non_func(200)
X_test = non_func(100)

# izgradnja neuronske mreže (potrebno ručno mijenjati brojeve neurona i reg. koef. zbog smanjenja vremena izvođenja)
reg = MLPRegressor(solver='adam', alpha=1e-4, hidden_layer_sizes=(1000,100), max_iter=1000)
reg.fit(X_train[:,0].reshape(-1,1), X_train[:,2])

#izgradnja linearnog reg. modela s polinomijalnim članovima
poly = PolynomialFeatures(1)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.fit_transform(X_test)
linearModel = lm.LinearRegression()
linearModel.fit(X_train_poly[:,:-1],X_train_poly[:,-1])

# predviđanje rezultata na testnom skupu
predictions = reg.predict(X_test[:,0].reshape(-1,1))
predictions_lin = linearModel.predict(X_test_poly[:,:-1])

#prikaz rezultata
plt.scatter(X_test[:,0], X_test[:,2], c='r')
plt.plot(X_test[:,0], predictions, c='b', label = 'Neural network')
plt.plot(X_test[:,0], predictions_lin, c='y', label = 'Linear reg.')
plt.plot(X_test[:,0], X_test[:,1], label = 'Real')
plt.legend()

print('MSE for neural network: %.2f' %mean_squared_error(X_test[:,-1], predictions))
print('MSE for linear regression: %.2f' %mean_squared_error(X_test[:,-1], predictions_lin))