import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather=pd.read_csv("C:/Users/ahake/Desktop/Codingal/Python/O^/Time Complexity/Weather Dataset.csv")
print(weather.head())

print(weather.info())

sns.barplot(weather['wind_speed'])
sns.barplot(weather['temperature'])
sns.displot(weather['temperature'])
sns.displot(weather['humidity'], rug=True)

plt.show()
