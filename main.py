import pandas as pd
import plotly.express as pt 

df = pd.read_csv("can_data.csv")

#Drops columns with the same value or all 0's 
for col in df.columns:
    if df[col].nunique(dropna = True) == 1 or (df[col] == 0).all():
        df.drop(col, axis = 1, inplace = True)

#RPM Graph
RPM_graph = pt.line(df, x = 'timestamp', y = 'RPM', title = 'RPM over time', labels = {'index':'Time', 'RPM': 'RPM'})
RPM_graph.show()

#TPS Graph
TPS_graph = pt.line(df, x = 'timestamp', y = 'TPS', title = 'TPS over time', labels = {'index':'Time', 'TPS': 'TPS'})
TPS_graph.show()
