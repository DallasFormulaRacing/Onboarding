import pandas as pd
import plotly.express as px

df = pd.read_csv('can-_ecu_762.csv')
analogColumns = df.loc[:,df.columns.str.contains('Analog Input')]
for  column in analogColumns.columns:
    if analogColumns[column].nunique() == 1:
        df.drop(columns=column, inplace=True)

df.to_csv('newData.csv')

RPM_Graph = px.line(df, x = 'timestamp', y = 'RPM', title = 'RPM graph')
TPS_Graph = px.line(df, x = 'timestamp', y = 'TPS', title = 'TPS graph')
RPM_Graph.show()
TPS_Graph.show()
