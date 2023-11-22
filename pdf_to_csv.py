import numpy as np
import tabula as ta
import pandas as pd

def pdf_to_csv(pdf_file_path, csv_file_path_prefix):
    """Converts a PDF spreadsheet to CSV."""
    try:
        # Read the PDF file into a list of DataFrames
        dfs = ta.read_pdf(pdf_file_path, pages='all')

        # Save each DataFrame as a separate CSV file
        for i, df in enumerate(dfs):
            csv_file_path = f"{csv_file_path_prefix}_{i}.csv"
            df.to_csv(csv_file_path, index=False)
            print(f"Saved {csv_file_path}")

        print("Conversion successful.")
    except Exception as e:
        print(f"Error: {e}")

# Get the PDF file on your local machine
pdf_file_path = "wypdf.pdf"

# Define a prefix for the output CSV files
csv_file_path_prefix = 'pdf_table'

print("The PDF spreadsheet is about to be converted to CSV.")

# Convert the PDF spreadsheet to CSV
pdf_to_csv(pdf_file_path, csv_file_path_prefix)

print("Conversion complete.")