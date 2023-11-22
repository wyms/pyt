import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the nvda.csv file
df = pd.read_csv("nvda.csv")

# Convert the "Date" column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Get the year from the "Date" column
df["Year"] = df["Date"].dt.year

# Calculate the yearly closing price
yearly_close = df.groupby("Year")["Close"].agg("mean")

# Plot the yearly closing price
plt.figure(figsize=(10, 6))
plt.plot(yearly_close.index, yearly_close.values)

# Add title and axis labels
plt.title("NVDA Stock Closing Price (Yearly)")
plt.xlabel("Year")
plt.ylabel("Close Price")

# Show the plot
plt.show()