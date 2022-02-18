from tiled.client.dataframe import DataFrameClient


class CustomObject:
    def __init__(self, df):
        self.df = df


def custom_client(*args, **kwargs):
    df = DataFrameClient(*args, **kwargs).read()
    return CustomObject(df)

