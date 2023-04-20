import numpy as np
import matplotlib as plt
import pandas as pd


class CommonEDA:
    def __init__(self, df: pd.DataFrame, target: str) -> None:
        self.numeric_cols = df.select_dtypes(
            include=np.number).columns.tolist()
        self.categorical_cols = df.select_dtypes(
            include=object).columns.tolist()
        self.df = df
        self.target = target

    def univariate_numeric(self):
        for col in self.numeric_cols:
            self.df[col].hist()
            plt.show()

    def univariate_categorical(self):
        for col in self.categorical_cols:
            self.df[col].value_counts().plot(kind='bar')
            plt.show()

    def bivariate_numeric(self):
        for col in self.numeric_cols:
            self.df.plot.scatter(x=col, y=self.target)
            plt.show()

    def bivariate_categorical(self):
        for col in self.categorical_cols:
            self.df.groupby(col)[self.target].mean().plot(kind='bar')
            plt.show()
