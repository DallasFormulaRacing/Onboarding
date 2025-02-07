import plotly.express as px

import pandas as pd

csv = "datadump.csv"
df = pd.read_csv(csv)

x = [f"Analog Input #{x}" for x in range(3,9)]

# print(x)
print(df.drop(x, axis = 1))

RPM = df["RPM"].tolist()
TPS = df["TPS"].tolist()
timeStamp = df["timestamp"].tolist()
RPM_GRAPH = px.line(y=RPM, x=timeStamp) 
TPS_GRAPH = px.line(y=TPS, x=timeStamp)

 
# printing the figure instance
RPM_GRAPH.show()
TPS_GRAPH.show()