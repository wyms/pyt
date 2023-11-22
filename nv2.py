import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the nvda.csv file
df = pd.read_csv("nvda.csv")

# Plot the close price
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Close"], label="Close")

# Add title and axis labels
plt.title("NVDA Stock Data")
plt.xlabel("Date")
plt.ylabel("Close Price")

# Show the plot
plt.show()