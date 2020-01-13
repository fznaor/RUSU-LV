import numpy as np

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