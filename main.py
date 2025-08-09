import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/content/startup_funding.csv")

print(df.head())
print(df.info())

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date column to datetime
df['date_dd/mm/yyyy'] = pd.to_datetime(df['date_dd/mm/yyyy'], errors='coerce')

# Drop rows where date is missing
df = df.dropna(subset=['date_dd/mm/yyyy'])

# Fill or drop other null values
df = df.copy() # Create a copy to avoid SettingWithCopyWarning
df['industry_vertical'] = df['industry_vertical'].fillna('Unknown')
df['city__location'] = df['city__location'].fillna('Unknown')
df['investors_name'] = df['investors_name'].fillna('Undisclosed')

# Remove commas, convert to numeric for amount
df['amount_in_usd'] = df['amount_in_usd'].replace('[\$,]', '', regex=True)
df['amount_in_usd'] = pd.to_numeric(df['amount_in_usd'], errors='coerce')

funding_trend = df.groupby(df['date_dd/mm/yyyy'].dt.to_period('M'))['amount_in_usd'].sum()
funding_trend.plot(kind='line', figsize=(12,6), marker='o')
plt.title("Funding Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Funding (USD)")
plt.show()

top_sectors = df['industry_vertical'].value_counts().head(10)
sns.barplot(x=top_sectors.values, y=top_sectors.index)
plt.title("Top 10 Sectors by Number of Fundings")
plt.xlabel("Number of Fundings")
plt.show()

top_cities = df['city__location'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index)
plt.title("Top 10 Cities by Number of Fundings")
plt.xlabel("Number of Fundings")
plt.show()

top_startups = df['startup_name'].value_counts().head(10)
sns.barplot(x=top_startups.values, y=top_startups.index)
plt.title("Top 10 Startups by Funding Count")
plt.xlabel("Number of Fundings")
plt.show()

active_investors = df['investors_name'].value_counts().head(10)
sns.barplot(x=active_investors.values, y=active_investors.index)
plt.title("Top 10 Active Investors")
plt.xlabel("Number of Investments")
plt.show()

sns.countplot(y='investmentntype', data=df, order=df['investmentntype'].value_counts().index)
plt.title("Investment Type Distribution")
plt.show()

print("\nRecommendations for Investors and Startup Founders:")
print("1. Focus on top-performing sectors like {}, which attract the most funding.".format(top_sectors.index[0]))
print("2. Cities like {} are hotspots for startups.".format(top_cities.index[0]))
print("3. Investment types like {} dominate, consider aligning strategies accordingly.".format(df['investmentntype'].mode()[0]))
print("4. Investors should monitor funding trends and target periods of high activity.")
