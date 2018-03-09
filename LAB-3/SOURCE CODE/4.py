from sklearn.metrics import accuracy_score
from sklearn import neighbors,datasets
from sklearn.model_selection import train_test_split

#the target variables are designed and assigned data
do =datasets.load_iris()
inf=do.data
labe=do.target
#Size_test data  20% training data 80%
ttrain, ttest, vtrain, vtest=train_test_splits(inf, labe, test_size=0.2, random_state=42)
kneign=neighbors.KNeighborsClassifier(n_neighbors=50) #Set
kneign.fit(ttrain, vtrain)
vprediction=kneign.predict(ttest)
#Calculate accuracy
print("Accuracy ", accuracy_score(vprediction, vtest))