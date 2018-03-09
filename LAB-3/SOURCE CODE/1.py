import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets


iris = datasets.load_iris()

t = iris.data
v = iris.target
target_named = iris.target_names

from sklearn.model_selection import train_test_split
t_train, t_test, v_train, v_test = train_test_split(t, v, test_size=0.30)

from sklearn.neighbors import KNeighborsClassifier
cc = KNeighborsClassifier(n_neighbors=5)
cc.fit(t_train, v_train)

v_pred = cc.predict(t_test)


ldaa1 = LinearDiscriminantAnalysis(n_components=2)
X2 = ldaa1.fit(t_test, v_pred).transform(t)

plt.figure()
colord = ['green', 'brown', 'orange']
law = 2


for clr, a, tar_name in zip(colord, [0, 1, 2], target_named):
    plt.scatter(X2[v == a, 0], X2[v == a, 1], alpha=.8, color=clr,
                label=tar_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA IRIS ')

plt.show()