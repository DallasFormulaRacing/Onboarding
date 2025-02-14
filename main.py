import plotly.express as px

import pandas as pd

csv = "datadump.csv"
df = pd.read_csv(csv)

x = [f"Analog Input #{x}" for x in range(3,9)]



# .drop(x, axis = 1)
# print(x)
analogInput = [x for x in df.columns if "Analog Input" in x]
for i in analogInput:
    switch = 0
    for k,j in enumerate(df[i]):
        if k == 0: continue
        if j != df.loc[k-1,i] and not pd.isna(j+df.loc[k-1,i]):
            switch = 1
            break
    if(switch == 0):    
        df = df.drop(i, axis = 1)
print(df)

RPM = df["RPM"].tolist()
TPS = df["TPS"].tolist()
timeStamp = df["timestamp"].tolist()
RPM_GRAPH = px.line(y=RPM, x=timeStamp) 
TPS_GRAPH = px.line(y=TPS, x=timeStamp)

 
# printing the figure instance
# RPM_GRAPH.show()
# TPS_GRAPH.show()