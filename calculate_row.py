# create function to count row
import pandas as pd

def read_csv(path):
    df = pd.read_csv(path, sep = ';')
    return df

def calculate_row(df):
    df = read_csv(path)
    row_len = len(df)
    return row_len

path = r'file/username.csv'

print(calculate_row(read_csv(path)))