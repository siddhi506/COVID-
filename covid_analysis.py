# ---------------------------------------
# COVID-19 Public Health Dashboard
# ---------------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("country_wise_latest(1).csv")

print("\n--- Dataset Preview ---")
print(df.head())

# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Remove missing values
df = df.dropna()

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

print("\n--- Dataset Info ---")
print(df.info())

# -------------------------------
# 3. Feature Engineering
# -------------------------------

# Calculate Death Rate and Recovery Rate
df['Death_Rate'] = df['Deaths'] / df['Confirmed']
df['Recovery_Rate'] = df['Recovered'] / df['Confirmed']

# -------------------------------
# 4. Region-wise Comparison
# -------------------------------
region_cases = df.groupby('WHO_Region')['Confirmed'].sum().sort_values()

plt.figure(figsize=(8,5))
region_cases.plot(kind='bar')
plt.title("Region-wise COVID-19 Confirmed Cases")
plt.xlabel("WHO Region")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("region_cases.png")   # save image
plt.show()

# -------------------------------
# 5. Top 10 Death Rate Countries
# -------------------------------
top_death = df.sort_values('Death_Rate', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_death['Country/Region'], top_death['Death_Rate'])
plt.title("Top 10 Countries by Death Rate")
plt.xlabel("Country")
plt.ylabel("Death Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("death_rate.png")
plt.show()

# -------------------------------
# 6. Top 10 Recovery Rate Countries
# -------------------------------
top_recovery = df.sort_values('Recovery_Rate', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_recovery['Country/Region'], top_recovery['Recovery_Rate'])
plt.title("Top 10 Countries by Recovery Rate")
plt.xlabel("Country")
plt.ylabel("Recovery Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("recovery_rate.png")
plt.show()

# -------------------------------
# 7. Pie Chart (Deaths vs Recovered)
# -------------------------------
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()

plt.figure(figsize=(6,6))
plt.pie([total_deaths, total_recovered],
        labels=["Deaths", "Recovered"],
        autopct='%1.1f%%')
plt.title("Deaths vs Recovered")
plt.savefig("pie_chart.png")
plt.show()

# -------------------------------
# 8. Save Processed Data
# -------------------------------
df.to_csv("processed_covid_data.csv", index=False)

print("\n--- Analysis Completed Successfully ---")
