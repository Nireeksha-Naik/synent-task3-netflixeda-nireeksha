# =====================================================
# NETFLIX EXPLORATORY DATA ANALYSIS (EDA)
# Synent Technologies Internship - Task 3
# =====================================================

# ---------- IMPORT LIBRARIES ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("\n========== IMPORTS SUCCESSFUL ==========")

# =====================================================
# LOAD DATASET
# =====================================================

print("\nLoading Dataset...")

df = pd.read_csv("netflix_titles.csv")

print("Dataset Loaded Successfully!")

# =====================================================
# BASIC INFORMATION
# =====================================================

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())

# =====================================================
# DATA CLEANING
# =====================================================

print("\n========== DATA CLEANING ==========")

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

print("Missing Values Filled Successfully!")

# Remove rows with missing dates
df = df.dropna(subset=['date_added'])

print("Rows with Missing Dates Removed!")

# Remove extra spaces from dates
df['date_added'] = df['date_added'].str.strip()

# Convert date column safely
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)

# Remove invalid dates if any
df = df.dropna(subset=['date_added'])

# Extract year
df['year_added'] = df['date_added'].dt.year

print("Date Conversion Completed!")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =====================================================
# SUMMARY STATISTICS
# =====================================================

print("\n========== SUMMARY STATISTICS ==========")

print(df.describe(include='all'))

# =====================================================
# VISUALIZATION FUNCTION
# =====================================================

def show_plot():
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

# =====================================================
# CONTENT TYPE ANALYSIS
# =====================================================

print("\nGenerating Content Type Analysis Graph...")

plt.figure(figsize=(6,4))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

show_plot()

print("Content Type Analysis Graph Completed!")

# =====================================================
# CONTENT RELEASE TREND
# =====================================================

print("\nGenerating Content Release Trend Graph...")

plt.figure(figsize=(12,6))

df['release_year'] \
    .value_counts() \
    .sort_index() \
    .tail(20) \
    .plot(kind='line')

plt.title("Content Released Over Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows/Movies")

show_plot()

print("Content Release Trend Graph Completed!")

# =====================================================
# TOP 10 COUNTRIES
# =====================================================

print("\nGenerating Top Countries Graph...")

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Count")
plt.ylabel("Country")

show_plot()

print("Top Countries Graph Completed!")

# =====================================================
# RATINGS DISTRIBUTION
# =====================================================

print("\nGenerating Ratings Distribution Graph...")

plt.figure(figsize=(10,5))

sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)

plt.title("Content Ratings Distribution")
plt.xlabel("Count")
plt.ylabel("Rating")

show_plot()

print("Ratings Distribution Graph Completed!")

# =====================================================
# MOVIES VS TV SHOWS OVER TIME
# =====================================================

print("\nGenerating Movies vs TV Shows Over Time Graph...")

content_year = df.groupby(['year_added', 'type']).size().unstack()

content_year.plot(figsize=(12,6))

plt.title("Movies and TV Shows Added Over Time")
plt.xlabel("Year")
plt.ylabel("Count")

show_plot()

print("Movies vs TV Shows Over Time Graph Completed!")

# =====================================================
# TOP GENRES
# =====================================================

print("\nGenerating Top Genres Graph...")

genres = df['listed_in'].str.split(', ', expand=True).stack()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")

show_plot()

print("Top Genres Graph Completed!")

# =====================================================
# CORRELATION HEATMAP
# =====================================================

print("\nGenerating Correlation Heatmap...")

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8,5))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

show_plot()

print("Correlation Heatmap Completed!")

# =====================================================
# KEY INSIGHTS
# =====================================================

print("\n========== KEY INSIGHTS ==========")

print("1. Netflix contains more Movies than TV Shows.")

print("2. The United States produces the highest amount of Netflix content.")

print("3. Content additions increased rapidly after 2015.")

print("4. Drama and International Movies are among the most common genres.")

print("5. TV-MA is one of the most frequent ratings.")

# =====================================================
# PROJECT SUMMARY
# =====================================================

print("\n========== PROJECT SUMMARY ==========")

print(f"Dataset Size: {df.shape}")

print(f"Total Content Count: {len(df)}")

print(f"Unique Ratings: {df['rating'].nunique()}")

print(f"Unique Genres: {top_genres.shape[0]}")

# =====================================================
# FINAL TERMINATION
# =====================================================

print("\n======================================")
print("PROJECT EXECUTED SUCCESSFULLY!")
print("Netflix EDA Completed Successfully.")
print("Program Terminated Successfully.")
print("======================================")