import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Load data
df = pd.read_csv("can-_ecu_762.csv")

#Remove all "analog input" columns with constant value
constant_columns = [col for col in df.columns if 'Analog Input' in col and df[col].nunique() == 1]
df_cleaned = df.drop(columns=constant_columns)

#Save cleaned data
df_cleaned.to_csv("cleaned_can_ecu.csv", index=False)

#Ensure timestamp exists
if 'timestamp' not in df_cleaned.columns:
    df_cleaned.insert(0, 'timestamp', df_cleaned.index) 

#Create separate subplots for RPM and TPS
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("RPM Over Time", "TPS Over Time")) 

#Add RPM graph
if 'RPM' in df_cleaned.columns:
    fig.add_trace(go.Scatter(x=df_cleaned['timestamp'], y=df_cleaned['RPM'], name="RPM", line=dict(color='#82C8F6')), row=1, col=1)

#Add TPS graph
if 'TPS' in df_cleaned.columns:
    fig.add_trace(go.Scatter(x=df_cleaned['timestamp'], y=df_cleaned['TPS'], name="TPS", line=dict(color='#98D8AF')), row=2, col=1)

#Make layout more readable
fig.update_layout(title_text="RPM and TPS Over Time", xaxis_title="Time", height=600, hovermode="x unified")

#Show the graph
fig.show()