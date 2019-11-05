import csv
import pandas as pd

csvPath = input('Enter CSV path: ')

df = pd.read_csv(csvPath,header=None)
df = df.iloc[::5]
df.to_csv(csvPath)