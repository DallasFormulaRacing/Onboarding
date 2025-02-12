#import pandas and plotly
import math
import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#read the csv file using pandas
filename = "can-_ecu_762.csv"
df = pd.read_csv(filename)
column_names = df.columns[1:9] #put column names into an array

#future reference
df.iloc[0] #first row of data 

#filter mech - detect and remove dead sensor data
outputList = []

for col in column_names: #repeat for each column
    outputList = [] #resets the array back after each column is checked
    test2 = df[col]
    for t in test2:
        #loop through the column (represented as a list)
        #find how many changes in the reading there are in each column. Ignore blanks
        if t not in outputList and not math.isnan(t): #see if there's a new value apart from the ones in the list (which is not blank)
            outputList.append(t)
    

    #check outputList to see if only one value has been stored (dead sensor detection)
    #if more than one value has been stored, then the loop can proceed to the next column

    if len(outputList) > 1:
        continue
    else:
        #delete that column (should drop Analog Inputs #3, 5, 7 and 8)
        df.drop(col, axis=1, inplace=True)
        df.to_csv(filename, index=False)

#graph RPM and TPS with respect to the time frame

RPM = df["RPM"] #stores RPM as an array, y1

TPS = df["TPS"] #same with TPS, y2

timeframe = df["timestamp"] #timestamp as the x axis

#allow a secondary y axis
graph = make_subplots(specs=[[{"secondary_y" : True}]])

#Initialize the first y axis:  RPM
graph.add_trace(
    go.Line(name="RPM", x=timeframe, y=RPM),
    secondary_y=False,
)

#initialize the second y axis: TPS
graph.add_trace(
    go.Line(name="TPS", x=timeframe, y=TPS),
    secondary_y = True,
)

#add a title to the graph
graph.update_layout(title_text="RPM & TPS vs timeframe")

graph.show()