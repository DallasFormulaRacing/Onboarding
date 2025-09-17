# importing libraries (pandas and plotly)
import pandas as pd
import plotly.express as px

# opening csv file and removing dead analog inputs
df = pd.read_csv('dfr_data.csv')
df.dropna()

# creating line chart based on RPM column and timestamp column
fig = px.line(df, x='timestamp', y='RPM', title="RPM over time", labels={"timestamp":"Time", "RPM":"RPM"}) 
fig.show()
