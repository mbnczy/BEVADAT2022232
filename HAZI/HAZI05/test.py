from HAZI05 import KNNClassifier

knn = KNNClassifier(3, 0.2)

x, y = knn.load_csv("iris.csv")

# knn.train_test_split(x, y)
# knn.predict()
#
# print(knn.accuracy)
