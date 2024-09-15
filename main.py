import pandas as pd
import plotly.express as px 
pd.options.plotting.backend = "plotly"

dataFrame = pd.read_csv('can-_ecu_762.csv')
editedDataFrame = dataFrame

for col in dataFrame:

    isUniqueRow = False
    for row in range(len(dataFrame)):
        
        if (dataFrame.at[row, col] != dataFrame.at[0,col]):
            isUniqueRow = True

    if(isUniqueRow == False):
        editedDataFrame = dataFrame.drop([col], axis=1)

rpmGraph = px.line(editedDataFrame, x="timestamp", y="RPM", title="RPM vs. Time")
tpsGraph = px.line(editedDataFrame, x="timestamp", y="TPS", title="TPS vs. Time")

rpmGraph.show()
tpsGraph.show()
