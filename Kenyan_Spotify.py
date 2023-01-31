import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("kenyan_spotify_music_streams.csv")

# Pre-processing
df['date'] = pd.to_datetime(df['date'])
df['streams'] = df['streams'].astype(int)

# Exploratory Data Analysis
plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='streams', data=df)
plt.title("Kenyan Spotify Music Streams Over Time")
plt.xlabel("Date")
plt.ylabel("Streams")
plt.show()

# Group the data by month
grouped = df.groupby(df['date'].dt.strftime('%B'))['streams'].sum()

# Visualize the monthly streams
plt.figure(figsize=(12,6))
sns.barplot(x=grouped.index, y=grouped.values)
plt.title("Monthly Kenyan Spotify Music Streams")
plt.xlabel("Month")
plt.ylabel("Streams")
plt.xticks(rotation=90)
plt.show()

# Calculate the top 5 artists with the most streams
top_artists = df.groupby('artist')['streams'].sum().sort_values(ascending=False).head(5)

# Visualize the top 5 artists
plt.figure(figsize=(12,6))
sns.barplot(x=top_artists.index, y=top_artists.values)
plt.title("Top 5 Kenyan Spotify Artists by Streams")
plt.xlabel("Artist")
plt.ylabel("Streams")
plt.xticks(rotation=90)
plt.show()
