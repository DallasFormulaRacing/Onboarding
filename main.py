import pandas as pd
import plotly.express as px

# Putting stuff into variables and pandas dataframe and changing settings.
file_path = "can_data.csv"
df = pd.read_csv(file_path)
dropped_columns = []

# This part cleans the dataframe
for column in df.columns:
    if 'Analog Input' in column and df[column].nunique() == 1:
        dropped_columns.append(column)

cleaned_df = df.drop(columns = dropped_columns)

# This part plots the dataframe data onto a graph and displays the graph.
fig_rpm = px.line(cleaned_df, x='timestamp', y='RPM')
fig_rpm.show()
fig_tps = px.line(cleaned_df, x='timestamp', y='TPS')
fig_tps.show()

# googoo gaagaa