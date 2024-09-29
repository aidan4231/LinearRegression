import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset= pd.read_csv("/Users/rausch/Desktop/Python/ai/data - Sheet1.csv")
print(dataset.head())
x = dataset.iloc[:,0:-1]
y = dataset.iloc[:,1]
Hours = dataset.iloc[:, 0:1]
assigments = dataset.iloc[:, 1:2]
lectures = dataset.iloc[:,2:3]
print(x)