# TASK 4: NETFLIX TREND ANALYSIS BY RELEASE YEAR

# STEP 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt

# STEP 2: Load the cleaned dataset

df = pd.read_csv("Netflix_Cleaned.csv")

# STEP 3: Display first five records

print("FIRST FIVE RECORDS:")
print(df.head())

# STEP 4: Display release year information

print("\nRELEASE YEAR INFORMATION:")
print(df["release_year"].head(10))

print("\nDATASET LOADED SUCCESSFULLY!")


# STEP 5: Count titles released each year

year_count = df["release_year"].value_counts().sort_index()

print("\nYEAR-WISE NETFLIX CONTENT COUNT:")
print(year_count)

# STEP 6: Find the top 10 release years

top_years = df["release_year"].value_counts().head(10)

print("\nTOP 10 YEARS:")
print(top_years)


# STEP 7: Create release-year trend chart

plt.figure(figsize=(12, 6))

year_count.plot(kind="line", marker="o")

plt.title("Netflix Content Release Trend by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)
plt.tight_layout()

plt.savefig("Task4_Release_Year_Trend.png")

plt.show()

print("\nTREND CHART CREATED SUCCESSFULLY!")


# STEP 8: Display key findings

highest_year = year_count.idxmax()
highest_count = year_count.max()

print("\n========== KEY FINDINGS ==========")
print("Total Release Years:", len(year_count))
print("Year with Highest Content:", highest_year)
print("Number of Titles:", highest_count)

print(
    "\nThe highest number of Netflix titles "
    "in the dataset was released in", highest_year
)

# STEP 9: Save yearly count as CSV

year_count.to_csv("Netflix_Year_Wise_Count.csv")

print("\nYEAR-WISE DATA SAVED SUCCESSFULLY!")
print("\nTASK 4 COMPLETED SUCCESSFULLY!")
