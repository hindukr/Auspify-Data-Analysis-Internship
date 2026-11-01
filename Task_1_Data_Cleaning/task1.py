#Code 1: Import Pandas and load the CSV file
 
# Step 1: Import Pandas
import pandas as pd

# Step 2: Load the Netflix dataset
df = pd.read_csv("Dataset.csv")

# Step 3: Display the first 5 records
print("FIRST FIVE RECORDS:")
print(df.head())


#Code 2: Display dataset information

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns)

# Display dataset information
print("\nDATASET INFORMATION:")
df.info()


#Code 3: Check missing values

# Check missing values in each column
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Calculate total missing values
total_missing = df.isnull().sum().sum()

print("\nTOTAL MISSING VALUES:")
print(total_missing)


#Code 4: Check and remove duplicates

# Count duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Display records after removing duplicates
print("\nDATASET AFTER DUPLICATE REMOVAL:")
print(df.shape)


#Code 5: Standardize data formatting

# Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Standardize content type
df["type"] = df["type"].str.title()

# Standardize ratings
df["rating"] = df["rating"].str.upper()

# Standardize country names
df["country"] = df["country"].str.title()

print("\nSTANDARDIZED DATA:")
print(df[["type", "country", "rating"]].head(10))


#Code 6: Export cleaned dataset

# Save the cleaned dataset
df.to_csv("Netflix_Cleaned.csv", index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as Netflix_Cleaned.csv")
