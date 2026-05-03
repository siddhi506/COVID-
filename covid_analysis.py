import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("country_wise_latest(1).csv")

# Clean data
df = df.dropna()
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Death & Recovery Rate
df['Death_Rate'] = df['Deaths'] / df['Confirmed']
df['Recovery_Rate'] = df['Recovered'] / df['Confirmed']

# Region-wise comparison
region = df.groupby('WHO_Region')['Confirmed'].sum()

region.plot(kind='bar')
plt.title("Region-wise COVID Cases")
plt.show()
