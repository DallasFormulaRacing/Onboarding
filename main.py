import pandas as pd
import plotly.express as pl

# read file
data_file = 'data.csv'
df = pd.read_csv(data_file)

# find the columns that we want to delete
analog_columns = [col for col in df.columns if 'Analog Input' in col]
delete_columns = [col for col in analog_columns if df[col].nunique() == 1]

# drop the columns
df.drop(columns=delete_columns)

# plot the data
RPM_graph = pl.line(df, x='timestamp', y='RPM', title='RPM vs Time')
TPS_graph = pl.line(df, x='timestamp', y='TPS', title='TPS vs Time')

# scatter plot to compare but no correlation
RPS_vs_TPS = pl.scatter(df, x='RPM', y='TPS', title='RPM vs TPS')

# show the plots
RPM_graph.show()
TPS_graph.show()
RPS_vs_TPS.show()