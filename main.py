import pandas as pd
import plotly.express as px


df = pd.read_csv('DataDump.csv')

removedCols = []
for col in df.columns:
    if 'Analog Input' in col and df[col].nunique() == 1:
        removedCols.append(col)

df = df.drop(columns=removedCols)

print(f"Unchanging columns: {removedCols}")

# RPM
fig_rpm = px.line(df, x='timestamp', y='RPM', title='RPM / Time')
fig_rpm.show()

# TPS
fig_tps = px.line(df, x='timestamp', y='TPS', title='TPS / Time')
fig_tps.show()