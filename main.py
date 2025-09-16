import pandas as pd
import plotly.express as px

#read the csv file with pandas
df = pd.read_csv("data.csv")

#clean the column names
df.columns = df.columns.str.strip()

#clean the data who have all same values in rows or NAN values
df = df.loc[:, lambda x: x.nunique() > 1]


#graph the data (RPM over time)
fig_rpm = px.line(df, x='timestamp', y = 'RPM', title="RPM over Time", labels={"timestamp":"Time", 'RPM': "RPM"})      

#graph TPS over time 
fig_tps = px.line(df, x = 'timestamp', y = 'TPS', title = "TPS over time", labels={"timestamp":"Time", "TPS": "TPS"})

#show the graphs
fig_rpm.show()
fig_tps.show()


