import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq  # Import the pyarrow.parquet submodule

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("sample_data.csv")

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Write the PyArrow Table to a Parquet file
pq.write_table(table, "my_data.parquet")  # Use pq.write_table instead of pa.write_table


#pq.write_table(table, "500_records.parqut")  # Use pq.write_table instead of pa.write_table
