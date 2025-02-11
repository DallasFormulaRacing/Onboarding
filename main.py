import pandas as pd
import plotly.express as px
# Load the CSV file
file_path = '/Users/krishjoshi/Desktop/datadumpExport2.csv'  # file is in the same directory as main.py
df = pd.read_csv(file_path, skiprows=1) # skip reading first row

#print(df.columns)
#print(df.head())

for column in df.columns:
    if df[column].nunique() == 1: # if number of unique values in col is 1...
        df.drop(column, axis=1, inplace=True)

output_file_path = 'datadumpExport_cleaned2.csv'
df.to_csv(output_file_path, index=False)



fig = px.line(df, x="timestamp", y="TPS").show()
fig = px.line(df, x="timestamp", y="RPM").show()

print(f"csv file cleaning worked at {output_file_path}")