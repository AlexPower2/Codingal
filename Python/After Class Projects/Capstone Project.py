import pandas as pd

# Load the dataset (update with your actual file path)
file_path = "IMDB Dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows
df.head()print("First three rows:")
print(df.head(3))

print("\nLast three rows:")
print(df.tail(3))df.info()print(df.isnull().sum()) # Count missing values in each columnsubset_df = df.iloc[41:76] # Since Python indexing starts from 0
print(subset_df.head()) # Display first few rows of the subsetmax_votes_movie = df[df["Votes"] == df["Votes"].max()]
print(max_votes_movie)import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["IMDB_Rating"], y=df["Runtime"])
plt.title("Box Plot of IMDB Rating vs Runtime")
plt.show()