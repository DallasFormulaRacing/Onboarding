"""
Programmer: Arav Neroth
Desc: remove all "analog inputs" that dont change values in the chart
"""
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

file = "can-_ecu_762.csv"
output = "sorted.csv"

engine = create_engine("sqlite://", echo = False)
df = pd.read_excel(file, sheet_name = "can-_ecu_762")
df.to_sql("Analog Input #1", engine, if_exists = "replace", index = False)

results = engine.execute("Select * from Analog Input #1")

final = pd.DataFrame(results, columns = df.columns)
final.to_excel(output, index = False)

print(final)