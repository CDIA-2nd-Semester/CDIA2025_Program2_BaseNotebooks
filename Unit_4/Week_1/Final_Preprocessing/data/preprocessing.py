import pandas as pd
import jupyter as jp


def preprocess_data(df):
    df=df.drop(['Id'], axis=1)
    # print("Sample of data")
    # print(df.sample(5))
    # print("Descritive statistics of data")
    # print(df.describe())
    df.dropna(inplace=True)
    # print("Data after dropping NA values")
    return df
