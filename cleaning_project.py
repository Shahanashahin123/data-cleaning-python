import pandas as pd

# Step 1: Create messy data
data = {
    'Name': [' John ', 'Anna', 'Bob', 'John ', 'Mia', None],
    'Age': [25, None, 30, 25, 22, 19],
    'City': ['new york', 'London', 'paris', 'new york', 'mumbai', 'delhi'],
    'Date_Joined': ['2024-01-05', '2024-03-10', '2024-02-20', '2024-01-05', '2024-05-11', '2024-06-13']
}

df = pd.DataFrame(data)
print("🧾 Original Data:\n", df)

# Step 2: Check missing values
print("\n🔍 Missing values in each column:\n", df.isnull().sum())

# Step 3: Fill missing values
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Step 4: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Clean text data
df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.title()

# Step 6: Fix data type
df['Date_Joined'] = pd.to_datetime(df['Date_Joined'])

# Step 7: Remove outliers
df = df[(df['Age'] >= 18) & (df['Age'] <= 90)]

# Step 8: Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

# Step 9: Print final result
print("\n✅ Cleaned Data:\n", df)
print("\n💾 Cleaned data saved to cleaned_data.csv")