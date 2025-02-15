import pandas as pd

# Load the dataset (update with your actual file path)
file_path = "Iris Dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows
df.head()import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.barplot(x="Species", y="SepalLengthCm", data=df)
plt.title("Bar Plot of Species vs Sepal Length")
plt.show()plt.figure(figsize=(6, 4))
sns.countplot(x="Species", data=df)
plt.title("Count Plot of Different Species")
plt.show()

sns.pairplot(df, hue="Species")
plt.show()