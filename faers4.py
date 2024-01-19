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

# Extract all reactions
try:
    # Split reactions based on semicolon
    reactions_split = df["Reactions"].str.lower().str.split(";")

    # Flatten the list of reactions
    reactions_flattened = reactions_split.explode()

    # Remove leading and trailing whitespaces
    reactions_cleaned = reactions_flattened.str.strip()

    # Count occurrences of all reactions
    top_reactions_counts = reactions_cleaned.value_counts().head(75)

    # Print the formatted results
    print("\nTop 25 most common reactions:")
    print(top_reactions_counts)
except KeyError:
    print("Error: Column 'Reactions' not found or accessible.")
