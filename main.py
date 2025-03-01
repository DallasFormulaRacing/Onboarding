"""
Programmer: Arav Neroth
Desc: remove all "analog inputs" that dont change values in the chart
"""
import pandas as pd
import sqlite3
import sqlalchemy

file = "can-_ecu_762.xlsx"
output = "sorted.xlsx"

# Create an in-memory SQLite database
engine = sqlalchemy.create_engine("sqlite://", echo=False)


# Fix table name: Remove spaces or enclose in quotes if needed
col_names = ["Analog_Input_1", "Analog_Input_2", "Analog_Input_3", "Analog_Input_4", 
             "Analog_Input_5", "Analog_Input_6", "Analog_Input_7", "Analog_Input_8"]

# Store DataFrame into the database
for col in col_names:
    df = pd.read_excel(file, sheet_name="can-_ecu_762")
    df.to_sql(col, engine, if_exists="replace", index=False)

final_dfs = []

with engine.connect() as conn:
    for col in col_names:
        results = conn.execute(sqlalchemy.text(f"SELECT * FROM {col}"))
        final_dfs.append(pd.DataFrame(results.fetchall(), columns=df.columns))

final = pd.concat(final_dfs, ignore_index=True)
final.to_excel(output, index=False)

print(final)
