import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select CSV File",
    filetypes=(("CSV Files", "*.csv"),)
)

if file_path:
    try:
        df = pd.read_csv(file_path)

        # Process and count reactions
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
        print("Error: File not found. Please ensure the selected file exists.")
    except pd.errors.EmptyDataError:
        print("Error: The specified CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: Unable to parse the CSV file. Please ensure it is a valid CSV file.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No file selected.")
