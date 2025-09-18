import pandas as pd
import plotly.express as px
import plotly.io as pio

#opens graph in a new tab
pio.renderers.default = "browser"

#data read and stored to df
df = pd.read_csv("can-_ecu_762.csv")

#loops through columns
for cols in df.columns:
    #checks whether the column contains a 0 or if there is a existing value
    if(df[cols]==0).all() or df[cols].nunique(dropna = True) == 1:
        #drops columns that have "dead sensors" or null
        df = df.drop(cols,axis = 1)

#makes and shows the graph for RPM
graph_RPM = px.line(df,x="timestamp", y="RPM", title = "RPM Graph")
graph_RPM.show()


#makes and shows the graph for TPS
graph_TPS = px.line(df,x="timestamp", y="TPS", title = "TPS Graph")
graph_TPS.show()