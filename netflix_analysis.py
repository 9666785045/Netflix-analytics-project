# Netflix Data Analysis Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Check number of rows and columns
print("\nDataset shape:", df.shape)

# Get info about the dataset
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Remove duplicate entries if any
df.drop_duplicates(inplace=True)

# Display column names
print("\nColumns in dataset:", df.columns.tolist())

# Summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

#visualizations
#count of movies vs tv shows
#This shows how many Movies vs TV Shows are available.

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Count of Movies vs TV Shows on Netflix')
plt.xlabel('Type of Content')
plt.ylabel('Count')
plt.show()


#Top 10 Countries with Most Netflix Titles
#Reveals where most Netflix content originates (likely the US, India, UK, etc.)

top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='crest')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

#Number of Releases by Year
#Shows how Netflix’s content library grew over time
plt.figure(figsize=(10,5))
df['release_year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Content Release Trend Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.show()

#Most Common Ratings
#Gives insight into the maturity level (TV-MA, PG, etc.) of most content
plt.figure(figsize=(8,4))
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='mako')
plt.title('Distribution of Netflix Content Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()

#Most Frequent Genres
#Tells which genres (like Dramas, Comedies, etc.) are most popular on Netflix.
from collections import Counter

# Split genres and count most common ones
genres = df['listed_in'].dropna().apply(lambda x: [i.strip() for i in x.split(',')])
genre_count = Counter([genre for sublist in genres for genre in sublist])
top_genres = dict(sorted(genre_count.items(), key=lambda x: x[1], reverse=True)[:10])
plt.figure(figsize=(10,5))
sns.barplot(x=list(top_genres.values()), y=list(top_genres.keys()), palette='viridis')
plt.title('Top 10 Most Common Netflix Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()


