import csv
import json

# Prompt for the CSV file
csv_file_path = input("Enter the path to the CSV file: ")

# Read the CSV data
with open(csv_file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row
    csv_data = list(reader)

# Convert the CSV data to a list of dictionaries
json_data = []
for row in csv_data:
    json_data.append({key: value for key, value in zip(header, row)})  # Dynamically create dictionary keys and values

# Print the JSON data to the console
print(json.dumps(json_data, indent=2))

# Write the JSON data to a new file
output_file_path = "output.json"  # Feel free to change the output file name
with open(output_file_path, "w") as outfile:
    json.dump(json_data, outfile, indent=2)

print(f"JSON data written to {output_file_path}")
