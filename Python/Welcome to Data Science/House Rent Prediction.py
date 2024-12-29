import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/ahake/Desktop/Codingal/Python/Welcome to Data Science/USA_Housing.csv")

print(df.head(10))
print(df.info())

print(df.describe())

print(df.columns)

sns.pairplot(df)
plt.show()

numeric_data=df.select_dtypes(include=["float64","int64"])
sns.heatmap(numeric_data.corr(),annot=True)
plt.show()
