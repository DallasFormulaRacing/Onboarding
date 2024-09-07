import pandas as pd
import plotly.express as px

file_path = './data.csv'
df = pd.read_csv(file_path)

analog_inputs = [col for col in df.columns if 'Analog Input' in col]
constant_columns = [col for col in analog_inputs if df[col].nunique() == 1]

df_cleaned = df.drop(columns=constant_columns)

graph_rpm = px.line(df_cleaned, x='timestamp', y='RPM', title='RPM vs Time')
graph_tps = px.line(df_cleaned, x='timestamp', y='TPS', title='TPS vs Time')

graph_rpm.show()
graph_tps.show()