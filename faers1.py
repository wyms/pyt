import pandas as pd

# Specify the file path
file_path = "/Users/wyoung/Desktop/python/ocrevus.csv"

# Read the CSV data into a DataFrame
df = pd.read_csv(file_path)

# Create a function to check if a reaction contains the word "cancer" (case-insensitive)
def has_cancer(reaction):
    return "cancer" in reaction.lower()

# Count the number of reactions containing "cancer"
cancer_count = df["Reactions"].apply(has_cancer).sum()

# Print the result
print(f"Number of cancers listed: {cancer_count}")
