import csv
import json

# Prompt for the JSON file
json_file_path = input("Enter the path to the JSON file: ")

# Read the JSON data
with open(json_file_path, "r") as jsonfile:
    json_data = json.load(jsonfile)

# Extract the header from the first data item
header = list(json_data[0].keys())

# Create the CSV data
csv_data = [header]  # Add the header row
for item in json_data:
    csv_data.append(list(item.values()))

# Prompt for the output CSV file
output_file_path = input("Enter the path to the output CSV file: ")

# Write the CSV data
with open(output_file_path, "w", newline="") as csvfile:  # Note: newline="" is important for Windows compatibility
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)

print(f"CSV data written to {output_file_path}")
