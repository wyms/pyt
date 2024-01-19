import pandas as pd

# Prompt the user for the file path
file_path = input("Enter the path to the CSV file: ")

# Read the CSV data into a DataFrame
try:
    df = pd.read_csv(file_path)

    # Process and count reactions
    try:
        reactions_cleaned = (
            df["Reactions"]
            .str.lower()
            .str.split(";")
            .explode()
            .str.strip()
        )
        top_counts = reactions_cleaned.value_counts().head(250)

        # Print the results to the console
        print(file_path)
        print("\nTop 250 most common reactions:")
        print(top_counts)

        # Write the results to a text file
        output_file_path = "top_200_reactions.txt"
        top_counts.to_csv(output_file_path, header=True)
        print(f"Top 250 reactions also saved to {output_file_path}")
    except KeyError:
        print("Error: Column 'Reactions' not found or accessible.")
except FileNotFoundError:
    print("Error: File not found. Please enter a valid file path.")
except pd.errors.EmptyDataError:
    print("Error: The specified CSV file is empty.")
except pd.errors.ParserError:
    print("Error: Unable to parse the CSV file. Please ensure it is a valid CSV file.")
