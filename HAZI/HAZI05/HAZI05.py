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

    def get_k(self):
        return self.k

    k_neighbors = property(fget=get_k)

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        df = pd.read_csv(csv_path, header=None)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = df.iloc[:, :8], df.iloc[:, -1]
        # x.fillna(3.5, inplace=True)
        # x = x.apply(pd.to_numeric, errors="coerce")
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        x_train, y_train = features[:train_size], labels[:train_size]
        x_test, y_test = features[train_size:], labels[train_size:]
        self.x_train = x_train.reset_index(drop=True)
        self.y_train = y_train.reset_index(drop=True)
        self.x_test = x_test.reset_index(drop=True)
        self.y_test = y_test.reset_index(drop=True)

    def euclidean(self, element_of_x: pd.DataFrame) -> pd.core.frame.DataFrame:
        return (((self.x_train - element_of_x) ** 2).sum(axis=1)) ** (1 / 2)

    def predict(self, x_test):
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(self, x_test.iloc[i]).tolist()
            for j in range(len(distances)):
                distances[j] = (distances[j], self.y_train[j])
            distances.sort(key=lambda a: a[0])
            distances = distances[: self.k]
            for h in range(len(distances)):
                distances[h] = distances[h][1]
            labels_pred.append(mode(distances, keepdims=False).mode.item())
        self.y_preds = pd.Series(labels_pred)

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def plot_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        # sns.heatmap(conf_matrix, annot=True)
        return conf_matrix

    def best_k(self) -> Tuple[int, float]:
        results = list()
        for i in range(1, 20):
            self.k = i
            self.predict(self, self.x_test)
            acc = round(self.accuracy(self), 2)
            results.append((i, acc))

        return max(results, key=lambda item: item[1])
