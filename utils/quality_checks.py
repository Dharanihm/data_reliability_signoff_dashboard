import pandas as pd


def duplicate_count(df):

    return df.duplicated().sum()


def missing_values(df):

    return df.isnull().sum() 