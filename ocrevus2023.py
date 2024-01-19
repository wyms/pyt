import pandas as pd

# Specify the file path (replace with your actual file path)
file_path = "/Users/wyoung/Desktop/python/ocrevus.csv"

# Read the CSV data into a DataFrame
df = pd.read_csv(file_path)

# Print column names and sample rows to visualize structure and content
print(df.columns)
print(df.head())

# Inspect the DataFrame for missing values (likely not relevant for this issue)
print(df.info())
if df["Reactions"].isnull().any():
    # Handle missing values (if needed):
    df["Reactions"].fillna("Unknown", inplace=True)

# Extract cancer types with the revised approach
try:
    # Split reactions based on semicolon
    reactions_split = df["Reactions"].str.lower().str.split(";")

    # Flatten the list of reactions
    reactions_flattened = reactions_split.explode()

    # Remove leading and trailing whitespaces
    reactions_cleaned = reactions_flattened.str.strip()

    # Filter reactions containing "cancer" and count occurrences
    cancer_counts = reactions_cleaned[reactions_cleaned.str.contains(r'\bcancer\b')].value_counts()

    # Print the formatted results
    print("\n2023 FAERS Ocrevus Reported Cases of Cancer:")
    print(cancer_counts)
except KeyError:
    print("Error: Column 'Reactions' not found or accessible.")
