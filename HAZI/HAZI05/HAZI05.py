import math
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns


class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float) -> None:
        self.k = k

    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        df = pd.read_csv(csv_path, header=None)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = df.iloc[:, :-1], df.iloc[:, -1]
        return x, y
