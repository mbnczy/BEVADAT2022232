# imports
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
import numpy as np
from scipy.stats import mode
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, confusion_matrix


class KMeansOnDigits:
    def __init__(self, n_clusters, random_state) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        model = KMeans(random_state=self.random_state, n_clusters=self.n_clusters)
        self.clusters = model.fit_predict(self.digits.data)

    def get_labels(self):
        result_array = np.empty(self.clusters.shape)
        for c in self.digits.target_names:
            mask = c == self.clusters
            sub_target = self.digits.target[mask]
            modus = mode(sub_target).mode.item()
            result_array[mask] = modus
        self.labels = result_array

    def calc_accuracy(self):
        self.accuracy = np.round(accuracy_score(self.digits.target, self.labels), 2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)
