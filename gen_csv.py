import csv
import random

# Define sample data
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
ages = [random.randint(20, 60) for _ in range(5000)]
cities = ["New York", "London", "Paris", "Tokyo", "Sydney", "Berlin", "Rome", "Moscow", "Toronto", "Seoul"]

# Shuffle the lists to ensure randomness
random.shuffle(names)
random.shuffle(cities)

# Create and write to CSV file
with open("sample_data.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(5000):
        writer.writerow({
            "Name": names[i % len(names)],
            "Age": ages[i],
            "City": cities[i % len(cities)]
        })
