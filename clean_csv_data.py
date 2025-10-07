import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("students.csv")
print("🧾 Original Data:\n", df)

# ------------------------------
#  🧠 BEFORE CLEANING SUMMARY
# ------------------------------
print("\n📋 Before Cleaning Summary:")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("Data Types:\n", df.dtypes)

# ------------------------------
#  🧹 CLEANING PROCESS
# ------------------------------

# Step 2: Handle missing values
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)

# Step 3: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 4: Clean text (remove spaces, fix capitalization)
df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.title()

# Step 5: Convert data types automatically
# (Ensures Age and Marks are numeric)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')

# Step 6: Remove outliers (optional example)
df = df[(df['Age'] >= 15) & (df['Age'] <= 100)]
df = df[(df['Marks'] >= 0) & (df['Marks'] <= 100)]

# Step 7: Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# ------------------------------
#  ✅ AFTER CLEANING SUMMARY
# ------------------------------
print("\n✅ After Cleaning Summary:")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("Data Types:\n", df.dtypes)

# Step 8: Save cleaned data
df.to_csv("students_cleaned.csv", index=False)

print("\n🎉 Data Cleaning Completed Successfully!")
print("💾 Cleaned file saved as 'students_cleaned.csv'")

# Step 9: Preview cleaned data
print("\n✨ Cleaned Data Preview:\n", df.head())
