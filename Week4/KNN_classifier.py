# supervised model, labeld data, value change hoile output kmn hobe ta bole deya ache, 
# classification er first model 
#iris flower data set to predict flower type

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
#print(iris.DESCR)

features=iris.data
labels=iris.target
#print(features[0], labels[0])

#training the classifier
clf=KNeighborsClassifier()
clf.fit(features, labels)

preds=clf.predict([[3.1,2,1,1]])
print(preds)
