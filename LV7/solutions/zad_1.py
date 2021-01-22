import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import sklearn.metrics as metrics
from sklearn import preprocessing

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

def plot_confusion_matrix(c_matrix, size):
    
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
    plt.title('Predvideno modelom (%s neurona u skrivenom sloju)' %size)
    plt.show()

# generiranje podataka i njihovo skaliranje
np.random.seed(242)
X_train = generate_data(200)
X_train = preprocessing.scale(X_train)
X_test = generate_data(100)
X_test = preprocessing.scale(X_test)

hidden_sizes = [1, 5, 10, 20, 50, 100]
reg_params = [0.001, 0.01, 0.1, 1, 10]

for i in range(len(hidden_sizes)): # za usporedbu regularizacijskih parametara potrebno promijeniti alpha koef. u reg_params[i]
    # generiranje neuronske mreže
    clf = MLPClassifier(solver='lbfgs', alpha=1, hidden_layer_sizes=(hidden_sizes[i]))
    clf.fit(X_train[:,0:2],X_train[:,2])
    
    # predviđanje klasa na testnom skupu
    predictions = clf.predict(X_test[:,0:2])
    
    # iscrtavanje dobivenih rezultata i granice odluke
    x_grid, y_grid = np.mgrid[min(X_train[:,0])-0.5:max(X_train[:,0])+0.5:.05,
                              min(X_train[:,1])-0.5:max(X_train[:,1])+0.5:.05]
    grid = np.c_[x_grid.ravel(), y_grid.ravel()]
    probs = clf.predict_proba(grid)[:, 1].reshape(x_grid.shape)
    
    cont = plt.contour(x_grid, y_grid, probs, 60, cmap="Greys", vmin=0, vmax=1, levels=[.5])
    plt.scatter(X_test[:,0],X_test[:,1],c=predictions)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('%s neurona u skrivenom sloju' %hidden_sizes[i])
    
    # iscrtavanje matrice zabune
    plot_confusion_matrix(metrics.confusion_matrix(X_test[:,2], predictions), hidden_sizes[i])
    
    # ispis mjera kvalitete klasifikacije
    print('%d neurona u skrivenom sloju:' %hidden_sizes[i])
    print('Accuracy = %.2f' %metrics.accuracy_score(X_test[:,2], predictions))
    print('Missclassification rate = %.2f' %(1-metrics.accuracy_score(X_test[:,2], predictions)))
    print('Precision = %.2f' %metrics.precision_score(X_test[:,2], predictions))
    print('Recall = %.2f' %metrics.recall_score(X_test[:,2], predictions))
    tn, fp, fn, tp = metrics.confusion_matrix(X_test[:,2], predictions).ravel()
    specificity = tn / (tn+fp)
    print('Specificity = %.2f\n' %specificity)