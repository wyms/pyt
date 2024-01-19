import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Set NSApplicationSupportsSecureRestorableState property for macOS
def set_secure_restorable_state():
    try:
        root = tk.Tk()
        root.createcommand("::tk::mac::OpenDocument", lambda: None)
        root.destroy()
    except Exception as e:
        print(f"Error: {e}")

# Call the function to set the property
set_secure_restorable_state()

# Use a Toplevel window instead of Tk() to avoid conflicts with the main loop
root = tk.Toplevel()
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

        # Generate the current datetime string
        current_datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Modify the output file path with datetime
        output_file_path = f"top_250_reactions_{current_datetime_str}.txt"

        # Print the results to the console
        print(file_path)
        print("\nTop 250 most common reactions:")
        print(top_counts)

        # Write the results to a text file with input file name on the first line
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Input File: {file_path}\n")
            top_counts.to_csv(output_file, header=True)

        print(f"Top 250 reactions also saved to {output_file_path}")

        # Destroy the Toplevel window to exit the script
        root.destroy()

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
