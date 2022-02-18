import pandas
from tiled.adapters.dataframe import DataFrameAdapter


class MyFileAdapter(DataFrameAdapter):
    specs = ["special_thing"]

    @classmethod
    def from_file(cls, filepath):
        """
        Expect a particular format like:

        key=<interger>
        key=<interger>
        ...
        --
        <csv>
        """
        file = open(filepath)
        metadata = {}
        for line in file:
            if line.startswith("-"):
                break
            key, _, value = line.partition("=")
            metadata[key] = int(value[:1])  # trim newline and convert to int
        # Parse the remaining lines with pandas.
        df = pandas.read_csv(file)
        return cls.from_pandas(df, metadata=metadata, npartitions=1)
