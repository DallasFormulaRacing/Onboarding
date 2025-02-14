#Neccesary libraries
import pandas as pd
import plotly.express as px 

#Reads the csv file by putting it into a pandas data frame
df = pd.read_csv('dataDumpFile.csv')

#placing all the analog input columns in an array
analogColumns = ['Analog Input #1','Analog Input #2','Analog Input #3','Analog Input #4','Analog Input #5','Analog Input #6','Analog Input #7','Analog Input #8']

#identifies the columns that need to be dropped: columns that exist in df have only one unique value
cols_to_drop = [col for col in analogColumns if col in df.columns and len(df[col].unique()) == 1]

#drops the columns
df.drop(columns=cols_to_drop, inplace=True)

#creates the RPM Graph
figRPM = px.line(df, x='timestamp', y='RPM', title='RPM Graph',
labels = {
 "timestamp": "Time",
})
figRPM.show()

#creates the TPS Graph
figTPS = px.line(df, x='timestamp', y='TPS', title='TPS Graph',
labels = {
 "timestamp": "Time",
})
figTPS.show()

