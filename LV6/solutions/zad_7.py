import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from matplotlib.colors import LinearSegmentedColormap
import sklearn.metrics as metrics

def plot_confusion_matrix(c_matrix):
    
    norm_conf = []
    for i in c_matrix:
        a = 0
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/float(a))
        norm_conf.append(tmp_arr)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    res = ax.imshow(np.array(norm_conf), cmap=plt.cm.Greys, interpolation='nearest')

    width = len(c_matrix)
    height = len(c_matrix[0])

    for x in range(width):
        for y in range(height):
            ax.annotate(str(c_matrix[x][y]), xy=(y, x), 
                        horizontalalignment='center',
                        verticalalignment='center', color = 'green', size = 20)

    fig.colorbar(res)
    numbers = '0123456789'
    plt.xticks(range(width), numbers[:width])
    plt.yticks(range(height), numbers[:height])
    
    plt.ylabel('Stvarna klasa')
    plt.title('Predvideno modelom')
    plt.show()


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

from sklearn.preprocessing import PolynomialFeatures
dgr = 3
poly = PolynomialFeatures(degree=dgr, include_bias = False)
X_train_new = poly.fit_transform(X_train[:,0:2])
X_train_new = np.append(X_train_new, X_train[:,2:3], axis=1)
X_test_new = poly.fit_transform(X_test[:,0:2])
X_test_new = np.append(X_test_new, X_test[:,2:3], axis=1)

logReg = lm.LogisticRegression()
logReg.fit(X_train_new[:, 0:-1], X_train_new[:,-1])


x_grid, y_grid = np.mgrid[min(X_train[:,0])-0.5:max(X_train[:,0])+0.5:.05,
                          min(X_train[:,1])-0.5:max(X_train[:,1])+0.5:.05]
grid = np.c_[x_grid.ravel(), y_grid.ravel()]
grid = poly.fit_transform(grid)
probs = logReg.predict_proba(grid)[:, 1].reshape(x_grid.shape)

#3. zadatak
plt.figure(1)
cont = plt.contour(x_grid, y_grid, probs, 60, cmap="Greys", vmin=0, vmax=1, levels=[.5])
plt.scatter(X_train[:,0], X_train[:,1], c = X_train[:,2])

plt.xlabel('$x_1$', alpha=0.9)
plt.ylabel('$x_2$', alpha=0.9)
plt.title('Izlaz logisticke regresije')

#4. zadatak
f, ax = plt.subplots(figsize=(8, 6))

cont = ax.contourf(x_grid, y_grid, probs, 60, cmap="Greys", vmin=0, vmax=1)
ax.scatter(X_train[:,0], X_train[:,1], c = X_train[:,2], cmap= 'inferno')

ax_c = f.colorbar(cont)
ax_c.set_label("$P(y = 1|\mathbf{x})$")
ax_c.set_ticks([0, .25, .5, .75, 1])
ax.set_xlabel('$x_1$', alpha=0.9)
ax.set_ylabel('$x_2$', alpha=0.9)
ax.set_title('Izlaz logisticke regresije')
plt.show()

#5. zadatak
predictions = logReg.predict(X_test_new[:, 0:-1])

plt.figure(3)
cont = plt.contour(x_grid, y_grid, probs, 60, cmap="Greys", vmin=0, vmax=1, levels=[.5])
plt.scatter(X_test[:,0], X_test[:,1], c = X_test[:,2] == predictions, cmap = LinearSegmentedColormap.from_list('mycmap', ['green', 'black']))
plt.xlabel('x1')
plt.ylabel('x2')
plt.ylabel('Rezultati na testnom skupu')

#6. zadatak
plot_confusion_matrix(metrics.confusion_matrix(X_test[:,2], predictions))

print('Accuracy = %.2f' %metrics.accuracy_score(X_test[:,2], predictions))
print('Missclassification rate = %.2f' %(1-metrics.accuracy_score(X_test[:,2], predictions)))
print('Precision = %.2f' %metrics.precision_score(X_test[:,2], predictions))
print('Recall = %.2f' %metrics.recall_score(X_test[:,2], predictions))
tn, fp, fn, tp = metrics.confusion_matrix(X_test[:,2], predictions).ravel()
specificity = tn / (tn+fp)
print('Specificity = %.2f' %specificity)