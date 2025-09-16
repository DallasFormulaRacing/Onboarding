# Read CSV via pandas
# Change both RPM and TPS to Arrays
# Make a for loop
# Run RPM and TPS through that loop, removing null values
# Take those values and graph it via Plotly

import pandas as pd
import plotly.express as px
import datetime as dt

# All Data
data = pd.DataFrame(pd.read_csv("can_data.csv", usecols=['timestamp', 'RPM', 'TPS']))
data['Datetime'] = pd.to_datetime(data['timestamp'], unit='s')


# Remove Null Values
data = data.dropna();
print(data)

# Plot Dataframes as a line graph
rpmPlot = px.line(data, x = 'Datetime', y = "RPM", title = "RPM over Time");
tpsPlot = px.line(data, x = 'Datetime', y = "TPS", title = "TPS over Time");

# # Show Data on Graph
rpmPlot.show()
tpsPlot.show()