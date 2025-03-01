"""
Programmer: Arav Neroth
Desc: remove all "analog inputs" that dont change in the 
"""
import pandas as pd
import sqlite3

csv_file = "can-_ecu_762.csv"  
df = pd.read_csv(csv_file)

# Create SQLite connection in memory (or use a file-based database)
conn = sqlite3.connect(":memory:")
df.to_sql("sensor_data", conn, index=False, if_exists="replace")

# Identify Analog Input columns that do not change
cursor = conn.cursor()
constant_columns = []
for column in df.columns:
    if column.startswith("Analog Input"):  # Adjust if necessary
        query = f"SELECT COUNT(DISTINCT \"{column}\") FROM sensor_data"
        cursor.execute(query)
        unique_values = cursor.fetchone()[0]
        if unique_values == 1:  # Column has only one unique value
            constant_columns.append(column)

# Drop constant columns
df_filtered = df.drop(columns=constant_columns)

# Save the cleaned CSV
filtered_csv_file = "filtered_sensor_data.csv"
df_filtered.to_csv(filtered_csv_file, index=False)

# Close the database connection
conn.close()

print(f"Filtered CSV saved as: {filtered_csv_file}")
print(f"Removed constant columns: {constant_columns}")
