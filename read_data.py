import pandas as pd
import matplotlib.pyplot as plt

raw_olympics = pd.read_csv("Olympics Data Transformed.csv")

raw_olympics.describe()
max_value = raw_olympics.max()

