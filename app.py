import pandas as pd


def read_csv(path):
    df = pd.read_csv(path, sep = ';')
    return df

path = r'file/username.csv'

print(read_csv(path))