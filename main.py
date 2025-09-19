print("hello world my changes")

import pandas as pd

df = pd.read_csv('can_data.csv')

analog_input_columns = [col for col in df.columns if 'Analog Input' in col]


columns_to_remove = []

for col in analog_input_columns:
    
    if df[col].nunique() == 1: 
        
        columns_to_remove.append(col)
    
df_cleaned = df.drop(columns=columns_to_remove)

import plotly.express as px

# RPM 
fig_rpm = px.line(df_cleaned, x='timestamp', y='RPM')
fig_rpm.update_layout(title='RPM Change Over Time', xaxis_title='Time', yaxis_title='RPM')
fig_rpm.show()

# TPS 
fig_tps = px.line(df_cleaned, x='timestamp', y='TPS')
fig_tps.update_layout(title='TPS Change Over Time', xaxis_title='Time', yaxis_title='TPS')
fig_tps.show()
