import math
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

filename = "can-_ecu_762.csv"
df = pd.read_csv(filename)

column_names = df.columns[1:9]  #filters the Analog Input Columns EXCLUSIVELY

# Detect and remove dead sensor data using nunique()
dead_sensors = df[column_names].nunique(dropna=True) == 1  # Drops nan values and finds which columns have dead sensors
df.drop(dead_sensors[dead_sensors].index, axis=1, inplace=True)  # Drop those columns

# Push this dataset to another file
df.to_csv("can-ecu_762_copy.csv", index=False)

# Graph RPM and TPS with respect to the timeframe
RPM = df["RPM"]  # Stores RPM as an array
TPS = df["TPS"]  # Stores TPS as an array
timeframe = df["timestamp"]  # Timestamp as the x-axis

# Allow a secondary y-axis
graph = make_subplots(specs=[[{"secondary_y": True}]])

# Initialize the first y-axis: RPM
graph.add_trace(
    go.Line(name="RPM", x=timeframe, y=RPM),
    secondary_y=False,
)

# Initialize the second y-axis: TPS
graph.add_trace(
    go.Line(name="TPS", x=timeframe, y=TPS),
    secondary_y=True,
)

# Add a title to the graph
graph.update_layout(title_text="RPM & TPS vs Timeframe")

graph.show()
