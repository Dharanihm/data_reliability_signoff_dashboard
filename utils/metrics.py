import pandas as pd


def completeness(df):

    missing = df.isna().sum().sum()

    total = df.size

    return round((1 - missing / total) * 100,2)


def freshness(df):

    df["last_updated"] = pd.to_datetime(df["last_updated"])

    latest = df["last_updated"].max()

    return latest.strftime("%Y-%m-%d %H:%M:%S")


def reconciliation(source, warehouse):

    return len(source) - len(warehouse) 