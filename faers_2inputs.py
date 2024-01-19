import pandas as pd

# Prompt the user for the file path and term
file_path = input("Enter the path to the CSV file: ")
term_to_count = input("Enter the term to count: ")

# Read the CSV data into a DataFrame
try:
    df = pd.read_csv(file_path)

    # Process and count the term occurrences
    try:
        reactions_cleaned = (
            df["Reactions"]
            .str.lower()
            .str.split(";")
            .explode()
            .str.strip()
        )
        term_count = reactions_cleaned.str.count(term_to_count).sum()

        # Print the results
        print(file_path)
        print(f"Count of '{term_to_count}': {term_count}")
    except KeyError:
        print("Error: Column 'Reactions' not found or accessible.")
except FileNotFoundError:
    print("Error: File not found. Please enter a valid file path.")
except pd.errors.EmptyDataError:
    print("Error: The specified CSV file is empty.")
except pd.errors.ParserError:
    print("Error: Unable to parse the CSV file. Please ensure it is a valid CSV file.")
