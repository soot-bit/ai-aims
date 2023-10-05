import pandas as pd
import numpy as np

filename = "./data/tutorial.csv"
df = pd.read_csv(filename)
print(df.head())
x = df['x'].to_numpy()
y = df['y'].to_numpy()
print(len(x))  # print number of elements

print("Hello world!")
