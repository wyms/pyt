import pandas as pd

# Specify the file path
file_path = "/Users/wyoung/Desktop/python/ocrevus.csv"


# Read the CSV data into a DataFrame
df = pd.read_csv(file_path)

# debugging
print(df.head())
print(df.columns)

# Extract cancer types from reactions (case-insensitive)
cancer_types = df["Reactions"].str.lower().str.extract(r"cancer\s+(.+)")  # Use raw string for regular expression

# Flatten the extracted lists
###cancer_types = cancer_types.explode("0")  # Explode the first column (index 0)
# Flatten the extracted lists (using the correct column name)
cancer_types = cancer_types.explode("Reactions")  # Replace "0" with "Reactions"

# Remove duplicates and count occurrences
cancer_counts = cancer_types.value_counts()

# Print the results
print("Cancer counts:")
print(cancer_counts)
