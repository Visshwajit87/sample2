import pandas as pd
from sklearn.datasets import fetch_california_housing
from IPython.display import display

data = fetch_california_housing(as_frame=True)
df = data.frame

display(df.head())
print("Shape of dataset:", df.shape)
df.info()
display(df.describe())
print("Missing values per column:")
print(df.isnull().sum())