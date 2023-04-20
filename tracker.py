import pandas as pd
import os
from typing import Union


class BaseTracker:
    TRACKER_PATH = "tracker/logs.csv"

    if not os.path.exists("tracker"):
        os.mkdir("tracker")

    if not os.path.exists(TRACKER_PATH):
        pd.DataFrame(columns=["model_name", "metric", "hyperparameters", "description", "model_path"]).to_csv(
            TRACKER_PATH, index=False)
        df = pd.read_csv(TRACKER_PATH)

    else:
        df = pd.read_csv(TRACKER_PATH)


class Tracker(BaseTracker):

    def add_logs(
            self,
            model_name: str,
            metric: list[tuple[str, float]],
            hyperparameters: dict[str, Union[str, float]],
            description: str,
            model_path: str = None):
        # self.df = self.df.append({
        #     "model_name": model_name,
        #     "metric": metric,
        #     "hyperparameters": hyperparameters,
        #     "description": description},
        #     ignore_index=True)
        self.df = pd.concat(
            [self.df,
             pd.DataFrame.from_records([{
                 "model_name": model_name,
                 "metric": metric,
                 "hyperparameters": hyperparameters,
                 "description": description,
                 "model_path": model_path if model_path else "None"
             }])], ignore_index=True
        )
        self.df.to_csv(self.TRACKER_PATH, index=False)

    def see_logs(self):
        return self.df
