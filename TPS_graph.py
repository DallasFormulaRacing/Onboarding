# importing libraries (pandas and plotly)
import pandas as pd
import plotly.express as px

# opening csv file and removing dead analog inputs
df = pd.read_csv('dfr_data.csv')
df.dropna()

# creating line chart based on TPS column and timestamp column
fig = px.line(df, x='timestamp', y='TPS', title="TPS over time", labels={"timestamp":"Time", "TPS":"TPS"}) 
fig.show()