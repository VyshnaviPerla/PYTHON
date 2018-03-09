from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston,load_digits
from scipy import sparse
from sklearn import svm
import numpy as np

C = 1.0
#get the data-response of dataset
#choose it
digs=load_digits() #load dataset
t=digs.data
v=digs.target
#splitting data to 20% test data, 80% train data
t_train, t_test, v_train, v_test=train_test_split(t, v, test_size=0.2)
#Apply SVC with Linear kernel
vd = svm.SVC(kernel='linear')
vd.fit(t_train, v_train)
v_pred=vd.predict(t_test)
print("SVC linear " + str(metrics.accuracy_score(v_test, v_pred)))
#SVC to R ker
vd = svm.SVC(kernel='rbf')
vd.fit(t_train, v_train)
v_pred=vd.predict(t_test)
print("Accuracy-SVC-rbf kernel " + str(metrics.accuracy_score(v_test, v_pred)))
