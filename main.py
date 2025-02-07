import plotly.express as px

import pandas as pd

csv = "datadump.csv"
df = pd.read_csv(csv)

x = [f"Analog Input #{x}" for x in range(3,9)]

# print(x)
print(df.drop(x, axis = 1))

RPM = df["RPM"].tolist()
TPS = df["TPS"].tolist()
RPM_GRAPH = px.line(RPM) 
TPS_GRAPH = px.line(TPS)

 
# printing the figure instance
RPM_GRAPH.show()
TPS_GRAPH.show()