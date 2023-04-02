import math
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns


class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float) -> None:
        self.k = k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self):
        return self.k

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        df = pd.read_csv(csv_path, header=None)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = df.iloc[:, :-1], df.iloc[:, -1]
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.Series) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "size mismatch!"
        self.x_train, self.y_train = (
            features.iloc[:train_size, :],
            labels.iloc[:train_size],
        )
        self.x_test, self.y_test = (
            features.iloc[train_size : train_size + test_size, :],
            labels.iloc[train_size : train_size + test_size],
        )

    def euclidean(self, element_of_x: pd.DataFrame):
        return (((self.x_train - element_of_x) ** 2).sum(axis=1)) ** (1 / 2)

    def predict(self):
        labels_pred = []
        for x_test_element in self.x_test.iterrows():
            distances = self.euclidean(self.x_train, x_test_element[1])
            distances = pd.concat([distances, self.y_train], axis=1)
            distances = distances.sort_values(by=[0])
            label_pred = mode(distances.iloc[: self.k, 1], axis=None)[0][0]
            labels_pred.append(label_pred)
        self.y_preds = pd.DataFrame(labels_pred, dtype=int)

    def accuracy(self) -> float:
        true_positive = (self.y_test.values == self.y_preds.values).sum()
        return true_positive / len(self.y_test) * 100

    def plot_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        sns.heatmap(conf_matrix, annot=True)
