import pandas as pd


def load_source():
    return pd.read_csv("data/source_system.csv")


def load_warehouse():
    return pd.read_csv("data/warehouse.csv")


def load_pipeline():
    return pd.read_csv("data/pipeline_log.csv") 