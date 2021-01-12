import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

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
    
    data  = np.concatenate((temp1,temp2),axis = 0)
    
    #permutiraj podatke
    indices = np.random.permutation(n)    
    data = data[indices,:]
    
    return data

np.random.seed(242)
X_train = generate_data(200)
X_test = generate_data(100)

logReg = lm.LogisticRegression()
logReg.fit(X_train[:, 0:2], X_train[:,2])

xp = np.array([X_train[:,0].min(), X_train[:,0].max()])
yp1 = -logReg.coef_[0][0]/logReg.coef_[0][1] * xp[0] - logReg.intercept_[0]/logReg.coef_[0][1]
yp2 = -logReg.coef_[0][0]/logReg.coef_[0][1] * xp[1] - logReg.intercept_[0]/logReg.coef_[0][1]
yp = np.array([yp1,yp2])

plt.scatter(X_train[:,0], X_train[:,1], c = X_train[:,2])
plt.plot(xp, yp)
plt.xlabel('x1')
plt.ylabel('x2')