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

# Test the regular expression's matching behavior
print(df["Reactions"].str.lower().str.extract(r";\s*cancer\s+(.+)"))

# Extract cancer types with the revised regular expression
try:
    cancer_types = df["Reactions"].str.lower().str.extract(r";\s*cancer\s+(.+)")

    # Flatten the extracted list
    cancer_types = cancer_types.explode("Reactions")

    # Remove duplicates and count occurrences
    cancer_counts = cancer_types.value_counts()

    # Print the results
    print("Cancer counts:")
    print(cancer_counts)
except KeyError:
    print("Error: Column 'Reactions' not found or accessible.")
    # Handle the error appropriately (e.g., provide a message or alternative actions)
