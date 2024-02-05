import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime

root = tk.Tk()
root.withdraw()

# This progam will take a CSV file as input and allow you to group and count based on one or more columns specified below
# In this example it will group by user, action

file_path = filedialog.askopenfilename(
    title="Select CSV File",
    filetypes=(("CSV Files", "*.csv"),)
)

if file_path:
    try:
        column_names = ["Date", "User", "Source Namespace Prefix", "Action", "Section", "Delegate User"]
        df = pd.read_csv(file_path, header=None, names=column_names)

        # Combine User and Action, clean, and count
        user_action_counts = (
            df[["User", "Action"]]
            .assign(Action=lambda x: x["Action"].str.lower().str.split(";").explode().str.strip())  # Clean actions
            .groupby(["User", "Action"])
            .size()
            .to_frame(name="Count")
            .reset_index()
        )

        ae_count = 400
        top_counts = user_action_counts.nlargest(ae_count, "Count")

        print(file_path)
        print("WY")
        print(ae_count)
        print(f"\nTop wytest {ae_count} most User + Action combinations:")
        print(top_counts)

        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_path = f"top_user_action_counts_{ae_count}_{current_datetime}.csv"
        top_counts.to_csv(output_file_path, header=True)

        print(f"Top {ae_count} User + Action counts also saved to {output_file_path}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No file selected.")
