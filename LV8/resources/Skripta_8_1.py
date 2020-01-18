import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn.externals import joblib
import pickle


mnist = fetch_mldata('MNIST original')
X, y = mnist.data, mnist.target

#print('Got MNIST with %d training- and %d test samples' % (len(X), len(y_test)))
#print('Image size is:')

# rescale the data, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: build youw own neural network using sckitlearn MPLClassifier 


# TODO: evaluate trained NN


# save NN to disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)

