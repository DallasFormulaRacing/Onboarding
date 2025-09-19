import pandas as pd
import plotly.express as px

#reads the data
data = pd.read_csv('can_data.csv')

#runs through all the columns and if they repeat the same input and are named alalog input they are dropped
for c in data.columns:
    if "Analog Input" in c and data[c].nunique() == 1:
        data.drop(columns = c, inplace = True)
        print("deleted" + c)

print(data.columns)

#creates a graph plotting two lines of TPS and RPM over time
fig = px.line(data, x = "timestamp", y = ["TPS","RPM"], title = "TPS and RPM over time")
fig.show()

