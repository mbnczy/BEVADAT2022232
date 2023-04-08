import pandas as pd
from datetime import datetime


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

    def convert_date_to_day(self) -> pd.DataFrame:
        # days = []
        # for i in range(len(self.data)):
        #    date_obj = datetime.strptime(self.data['date'][i], '%Y-%m-%d')
        #    day = date_obj.strftime('%A')
        #    days.append(day)
        # self.data['day'] = days
        newdata = self.data.copy()
        newdata = newdata.assign(
            day=self.data["date"].apply(
                lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%A")
            )
        )
        newdata.drop(["date"], axis=1, inplace=True)
        return newdata
