#Akash Dasarraju
#Github ID: Sky1219
#Discord ID: Samtin56
import pandas as pd
import plotly.express as px

#Input: Dataframe
#Output: Dataframe without NAN entries and dead analog sensors
def cleandata(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.dropna()
    dead_columns =[]
    #Removes columns with "Analog Input" in title and only one unique entry
    analog_input_cols = dataframe.filter(like='Analog Input').columns
    for col in analog_input_cols:
        if len(dataframe[col].unique()) == 1:
            dead_columns.append(col)
    if dead_columns:
        dataframe = dataframe.drop(columns=dead_columns)

    return dataframe

#Reads, cleans, and saves csv
canFrame = pd.read_csv('can_data.csv')
canFrame = cleandata(canFrame)
canFrame.to_csv("cleaned_can_data.csv", encoding='utf-8', index=False)

#Graphs
fig_rpm = px.line(canFrame, x='timestamp', y='RPM')
fig_tps = px.line(canFrame, x='timestamp', y='TPS')
fig_rpm.show()
fig_tps.show()
