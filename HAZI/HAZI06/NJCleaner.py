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
            day=newdata["date"].apply(
                lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%A")
            )
        )
        newdata.drop(["date"], axis=1, inplace=True)
        return newdata

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        newdata = self.data.copy()
        newdata["part_of_the_day"] = pd.to_datetime(
            newdata["scheduled_time"], errors="coerce"
        ).dt.hour.apply(
            lambda x: "early_morning"
            if 4 <= x <= 7
            else "morning"
            if 8 <= x <= 11
            else "afternoon"
            if 12 <= x <= 15
            else "evening"
            if 16 <= x <= 19
            else "night"
            if 20 <= x <= 23
            else "late_night"
        )
        newdata.drop(["scheduled_time"], axis=1, inplace=True)
        return newdata

    def convert_delay(self) -> pd.DataFrame:
        newdata = self.data.copy()
        newdata["delay"] = newdata["delay_minutes"].apply(
            lambda x: 0 if 0 <= x and x < 5 else 1
        )
        return newdata

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        newdata = self.data.copy()
        newdata.drop(
            ["train_id" "scheduled_time" "actual_time" "delay_minutes"],
            axis=1,
            inplace=True,
        )
        return newdata

    def save_first_60k(self, path: str):
        self.data.head(60000).to_csv(path)

    def prep_df(self, save_csv_path="data/NJ.csv"):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()

        try:
            self.data = self.drop_unnecessary_columns()
        except:
            print("drop error")

        self.data.to_csv(save_csv_path)
