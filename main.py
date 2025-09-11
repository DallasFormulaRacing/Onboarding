import pandas as pd
import plotly.express as px

#read the csv file with pandas
df = pd.read_csv("data.csv")

#clean the column names
df.columns = df.columns.str.strip()

#clean the data who have all same values in rows or NAN values
df = df.dropna(axis=1).loc[:, lambda x: x.nunique() > 1]

#keep the graphed data to the first 100 rows so that the graph can render
df_sampled = df.head(100)

#graph the data (RPM over time)
fig_rpm = px.line(df_sampled, x='timestamp', y = 'RPM', title="RPM over Time", labels={"timestamp":"Time", ' RPM': "RPM"})      

#graph TPS over time 
fig_tps = px.line(df_sampled, x = 'timestamp', y = 'TPS', title = "TPS over time", labels={"timestamp":"Time", " TPS": "TPS"})

#show the graph
fig_rpm.show()


