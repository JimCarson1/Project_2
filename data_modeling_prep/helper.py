import pandas as pd
import gzip
import os

def unzip_gz(path):
    """Unzips a .gz file and saves the result as a CSV file.

    Parameters:
    path (str): The file path of the .gz file to be unzipped.

    Example usage:
    unzip_gz('/path/to/file.gz')"""

    with gzip.open(path, 'rt') as f:
        df = pd.read_csv(f)
        return df

def zip_gz(df, path):
    """
    Compresses a file to a .gz format.

    Parameters:
    path (str): The file path to be compressed.

    Example usage:
    zip_gz(df, '/path/to/name_of_file.gz')
    Note: Include the file extension (.gz) at the end of the path.
    """

    df.to_csv(path, index=False, compression='gzip')

