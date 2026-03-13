import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('archive\India Agriculture Crop Production.csv')

# 2. Basic Exploration
print(df.head())
print(df.info())

# 3. Handling Missing Values (Crucial for freshers!)
df = df.dropna() 

# 4. A quick Visualization for your "Heatmap"
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='YlGnBu')
plt.title("Feature Correlation Heatmap")
plt.savefig('correlation_heatmap.png') # Save this for GitHub!
plt.show()

