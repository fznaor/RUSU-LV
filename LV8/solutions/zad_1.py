import numpy as np
import joblib
from sklearn.neural_network import MLPClassifier
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

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



def sort_by_target(mnist):
    reorder_train = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[:60000])]))[:, 1]
    reorder_test = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[60000:])]))[:, 1]
    mnist.data[:60000] = mnist.data[reorder_train]
    mnist.target[:60000] = mnist.target[reorder_train]
    mnist.data[60000:] = mnist.data[reorder_test + 60000]
    mnist.target[60000:] = mnist.target[reorder_test + 60000]

try:
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version=1, cache=True)
    mnist.target = mnist.target.astype(np.int8) # fetch_openml() returns targets as strings
    sort_by_target(mnist) # fetch_openml() returns an unsorted dataset
except ImportError:
    from sklearn.datasets import fetch_mldata
    mnist = fetch_mldata('MNIST original')

X, y = mnist.data, mnist.target

# rescale the data, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

print('Got MNIST with %d training- and %d test samples' % (len(X), len(y_test)))

# TODO: build youw own neural network using sckitlearn MPLClassifier 
mlp_mnist = MLPClassifier(solver='adam', alpha=0.1, hidden_layer_sizes=(50))
mlp_mnist.fit(X_train,y_train)

# TODO: evaluate trained NN
predictions = mlp_mnist.predict(X_test)

plot_confusion_matrix(metrics.confusion_matrix(y_test, predictions))

print('Accuracy = %.2f' %metrics.accuracy_score(y_test, predictions))
print('Missclassification rate = %.2f' %(1-metrics.accuracy_score(y_test, predictions)))
print('Precision = %.2f' %metrics.precision_score(y_test, predictions, average = 'macro'))
print('Recall = %.2f' %metrics.recall_score(y_test, predictions, average = 'macro'))


# save NN to disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)