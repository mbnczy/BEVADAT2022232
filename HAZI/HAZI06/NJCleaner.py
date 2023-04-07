import pandas as pd


class NJCleaner:
    def __init__(self, csv_path: str) -> None:
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        order = self.data.sort_values(by=["scheduled_time"])
        return order

    def drop_columns_and_nan(self) -> pd.DataFrame:
        newdata = self.data.drop(["from", "to"], axis=1)
        newdata.dropna(inplace=True)
        return newdata
