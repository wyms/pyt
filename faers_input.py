import pandas as pd

# Prompt the user to enter the file path
file_path = input("Enter the path to the CSV file: ")



# Read the CSV data into a DataFrame
try:
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
        top_reactions_counts = reactions_cleaned.value_counts().head(50)

        # Print the formatted results
        print(file_path)
        print("\nTop 50 most common reactions:")
        print(top_reactions_counts)
    except KeyError:
        print("Error: Column 'Reactions' not found or accessible.")
except FileNotFoundError:
    print("Error: File not found. Please enter a valid file path.")
except pd.errors.EmptyDataError:
    print("Error: The specified CSV file is empty.")
except pd.errors.ParserError:
    print("Error: Unable to parse the CSV file. Please ensure it is a valid CSV file.")
