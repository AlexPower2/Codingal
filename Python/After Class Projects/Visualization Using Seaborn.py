import pandas as pd

df = pd.read_csv("C:/Users/ahake/Desktop/Codingal/Python/After Class Projects/Tips Dataset.csv")


df.head()


df[['size', 'tip', 'total_bill']].describe()

import seaborn as sns
import matplotlib.pyplot as plt


sns.scatterplot(data=df, x='total_bill', y='tip', hue='time', palette='coolwarm')


plt.show()


sns.pairplot(df, hue='gender')


plt.show()
