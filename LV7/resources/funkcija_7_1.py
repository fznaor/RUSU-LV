import numpy as np

def generate_data(n):
	
	#prva klasa
	n1 = int(n/2)
	x1_1 = np.random.normal(0.0, 2, (n1,1));
	
	#x1_1 = .21*(6.*np.random.standard_normal((n1,1)));
	x2_1 = np.power(x1_1,2) + np.random.standard_normal((n1,1));
	y_1 = np.zeros([n1,1])
	temp1 = np.concatenate((x1_1,x2_1,y_1),axis = 1)
	
	#druga klasa
	n2 = int(n - n/2)
	x_2 = np.random.multivariate_normal((0,10), [[0.8,0],[0,1.2]], n2);
	y_2 = np.ones([n2,1])
	temp2 = np.concatenate((x_2,y_2),axis = 1)
	data = np.concatenate((temp1,temp2),axis = 0)
	
	#permutiraj podatke
	indices = np.random.permutation(n)
	data = data[indices,:]
	
	return data
