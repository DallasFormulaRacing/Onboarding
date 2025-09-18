import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#load csv file
try:
    df = pd.read_csv('can_data.csv')
    print("CSV file loaded")
except FileNotFoundError:
    print("Error: File 'can_data.csv' not found")
    exit()


#clean data
col_remove = []
for col in df.columns:
    if 'Analog Input' in col:
        if df[col].nunique() == 1:
            col_remove.append(col)
df.drop(columns=col_remove, inplace=True)
print(f"Removed columns: {col_remove}")

#line graph w/ labels
time_col = 'timestamp'
df[time_col] = pd.to_numeric(df[time_col], errors='coerce')
df.dropna(subset=[time_col], inplace=True)

graph_rpm = px.line(df, x=time_col, y='RPM')
graph_rpm.update_layout(title_text='RPM over Time', xaxis_title='Timestamp)', yaxis_title='RPM')
graph_rpm.show()

graph_tps = px.line(df, x=time_col, y='TPS')
graph_tps.update_layout(title_text='TPS over Time', xaxis_title='Timestamp', yaxis_title='TPS (%)')
graph_tps.show()