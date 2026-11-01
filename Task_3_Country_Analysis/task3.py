
# TASK 3: COUNTRY-WISE NETFLIX ANALYSIS

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("Netflix_Cleaned.csv")

# Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display country information
print("\nCOUNTRY INFORMATION:")
print(df["country"].head(10))

print("\nDATASET LOADED SUCCESSFULLY!")



# STEP 2: Remove unknown and missing countries

country_df = df[
    (df["country"] != "Unknown") &
    (df["country"].notna()) &
    (df["country"].str.strip() != "")
].copy()

# STEP 3: Split multiple countries

country_df["country"] = country_df["country"].str.split(",")

# STEP 4: Separate countries into individual rows

country_df = country_df.explode("country")

# STEP 5: Remove extra spaces

country_df["country"] = country_df["country"].str.strip()

# Display cleaned country data

print("\nCLEANED COUNTRY DATA:")
print(country_df[["title", "country"]].head(15))


# STEP 6: Count titles country-wise

country_count = country_df["country"].value_counts()

print("\nCOUNTRY-WISE CONTENT COUNT:")
print(country_count.head(20))


# STEP 7: Identify top 10 countries

top_countries = country_count.head(10)

print("\nTOP 10 COUNTRIES:")
print(top_countries)

# STEP 8: Remove Not Given from chart data

top_countries = top_countries[
    top_countries.index != "Not Given"
]

# STEP 9: Create bar chart

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

top_countries.sort_values().plot(
    kind="barh",
    color="skyblue"
)

plt.title("Top Netflix Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("Task3_Top_Countries.png")

plt.show()

print("\nBAR CHART CREATED SUCCESSFULLY!")