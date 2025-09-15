# Read CSV via pandas
# Change both RPM and TPS to Arrays
# Make a for loop
# Run RPM and TPS through that loop, removing null values
# Take those values and graph it via Plotly

import pandas as pd
import plotly.express as px

# Dataframes
rpm = pd.read_csv("can_data.csv", usecols=["timestamp", "RPM"]);
tps = pd.read_csv("can_data.csv", usecols=["timestamp", "TPS"]);

# Remove Null Values
rpm = rpm.dropna();
tps = tps.dropna();

# Plot Dataframes as a line graph
rpmPlot = px.line(rpm, x = "timestamp", y = "RPM", title = "RPM over Time");
tpsPlot = px.line(tps, x = "timestamp", y = "TPS", title = "TPS over Time");

# Show Data on Graph
rpmPlot.show()
tpsPlot.show()