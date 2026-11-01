#Load the cleaned dataset

# TASK 2: CONTENT TYPE ANALYSIS DASHBOARD

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load cleaned dataset
df = pd.read_csv("Netflix_Cleaned.csv")

# Step 3: Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

print("\nDATASET LOADED SUCCESSFULLY!")


#Calculate total Movies and TV Shows

# Step 4: Count Movies and TV Shows

content_count = df["type"].value_counts()

print("\nCONTENT TYPE COUNT:")
print(content_count)

# Calculate total records
print("\nTOTAL CONTENT:")
print(len(df))


#Calculate content percentages

# Step 5: Calculate content percentages

percentage = (content_count / len(df)) * 100

print("\nCONTENT TYPE PERCENTAGES:")
print(percentage.round(2))


#Create a Bar Chart

# Step 6: Create Bar Chart

plt.figure(figsize=(8, 5))

content_count.plot(kind="bar")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.xticks(rotation=0)

plt.tight_layout()

# Save chart
plt.savefig("Task2_Bar_Chart.png")

# Display chart
plt.show()


#Create a Pie Chart

# Step 7: Create Pie Chart

plt.figure(figsize=(7, 7))

content_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Distribution")

plt.ylabel("")

plt.tight_layout()

# Save pie chart
plt.savefig("Task2_Pie_Chart.png")

# Display chart
plt.show()


#Summarize your key findings

# Step 8: Summarize Key Findings

print("\n========== KEY FINDINGS ==========")

movie_count = content_count.get("Movie", 0)
tv_count = content_count.get("Tv Show", 0)

movie_percentage = percentage.get("Movie", 0)
tv_percentage = percentage.get("Tv Show", 0)

print("Total Netflix Titles:", len(df))

print("Total Movies:", movie_count)
print("Total TV Shows:", tv_count)

print("Movie Percentage:", round(movie_percentage, 2), "%")
print("TV Show Percentage:", round(tv_percentage, 2), "%")

if movie_count > tv_count:
    print("\nMovies are the most common content type.")
else:
    print("\nTV Shows are the most common content type.")

print("\nTASK 2 COMPLETED SUCCESSFULLY!")
