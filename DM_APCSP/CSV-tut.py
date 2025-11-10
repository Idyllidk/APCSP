#Import all necessary libraries - PD, PLT, and NP
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Create our dataframe using our csv
data = pd.read_csv(r"DM_APCSP\apcspb3.csv")


df = pd.DataFrame(data)

print("-_"*40)
print("Head of the Data Frame:")
print(df.head())

print("-_"*40)
print("Tail of the Data Frame:")
print(df.tail())

print("-_"*40)
print("Information about the Data Frame:")
print(df.info())

print("-_"*40)
print(round(df.describe(),1))

print("-_"*40)
print("Pie Value Counts")
print(df['PIE'].value_counts())

print("-_"*40)
print(df.groupby('PIE')['NAP'].mean())
