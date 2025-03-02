"""
Programmer: Arav Neroth
Desc: remove all "analog inputs" that dont change values in the chart
"""
import pandas as pd
import sqlalchemy
import random
import re
import plotly.express as plotly

'''
made a random number generator bc i kept generating excel files to see if it worked
and it kept crashing bc the name was the same so this just makes every file unique lol
'''

# sorting data
rand_num = random.randint(0, 9999)
unsorted_file = "can-_ecu_762.xlsx"
output = f"sorted{rand_num}.xlsx"

# using the sorted data for graphs
sorted_file = f"sorted{rand_num}"

# locally process this using SQLite
engine = sqlalchemy.create_engine("sqlite://", echo=False)

# add data and make it processable
sheet_name = "can-_ecu_762"
df = pd.read_excel(unsorted_file, sheet_name=sheet_name)
df.columns = df.columns.str.strip()

# look for columns that match "Analog Input #1", "Analog Input #2", etc.
analog_input_cols = [col for col in df.columns if re.match(r"Analog Input #\d+", col)]

# using said sorted columns above, see which ones do    n't have changing data
constant_cols = [col for col in analog_input_cols if df[col].nunique() == 1]

# remove em 
df = df.drop(columns=constant_cols)
print("Removed Columns:", constant_cols)

# store in the database
df.to_sql("filtered_data", engine, if_exists="replace", index=False)

# process the filtered data
with engine.connect() as conn:
    results = conn.execute(sqlalchemy.text("SELECT * FROM filtered_data"))
    final_df = pd.DataFrame(results.fetchall(), columns=df.columns)

# new sorted file!
final_df.to_excel(output, index=False)
print(f"Successfully processed and outputted in file: sorted{rand_num}.")

# very convienet graphing
fig = plotly.scatter(final_df, x="timestamp", y=["RPM", "TPS"], title="Scatter Plot of RPM & TPS over time")
print(f"Successfully plotted RPM & TPS to a scatterplot.")

fig2 = plotly.scatter(final_df, x="timestamp", y="RPM", title="Scatter Plot of RPM over time")
print(f"Successfully plotted RPM to a scatterplot.")

fig3 = plotly.scatter(final_df, x="timestamp", y="TPS", title="Scatter Plot of TPS over time")
print(f"Successfully plotted TPS to a scatterplot.")

print(f"Redirecting to browser to view.")

fig.show()
fig2.show()
fig3.show()
