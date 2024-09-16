import pandas as pd
import plotly.express as px

file_path = 'C:\\Users\\krish\\Downloads\\datadump.csv'
df = pd.read_csv(file_path)

# loop through each col
for column in df.columns:
    if df[column].nunique() == 1:
        df.drop(column, axis=1, inplace=True)

# save to new file
output_file_path = 'C:\\Users\\krish\\Downloads\\datadump_cleaned.csv'
df.to_csv(output_file_path, index=False)


px.line(df, x='timestamp', y='TPS').show()
px.line(df, x='timestamp', y='RPM').show()


print(f"clean csv at {output_file_path}")
