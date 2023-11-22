import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the sample image
data = [[pd.to_datetime("1993-07-22 0:00"), 22.75, 23, 22.625, 23, 4.602782, 3159100],
        [pd.to_datetime("1993-07-23 0:00"), 23, 23.625, 23, 23.25, 4.652814, 609900],
        [pd.to_datetime("1993-07-26 0:00"), 23.25, 23.25, 22.75, 22.75, 4.552753, 218400],
        [pd.to_datetime("1993-07-27 0:00"), 22.875, 22.875, 22.75, 22.75, 4.552753, 183800],
        [pd.to_datetime("1993-07-28 0:00"), 22.75, 23.125, 22.75, None, None, 192900]]

df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

# Plot the close price
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Close"], label="Close")

# Add title and axis labels
plt.title("NVDA Stock Data Sample")
plt.xlabel("Date")
plt.ylabel("Close Price")

# Show the plot
plt.show()