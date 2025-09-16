#Akash Dasarraju
#Github ID: Sky1219
#Discord ID: Samtin56
import pandas as pd
import plotly.express as px

#Input: Dataframe
#Output: Dataframe without NAN entries and dead analog sensors
def cleandata(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.dropna()
    dead_columns = []
    #Removes columns with "Analog Input" in title and only one unique entry
    analog_input_cols = dataframe.filter(like='Analog Input').columns
    for col in analog_input_cols:
        if len(dataframe[col].unique()) == 1:
            dead_columns.append(col)
    if dead_columns:
        print(f"Removing : {dead_columns}")
        dataframe = dataframe.drop(columns=dead_columns)
    else:
        print("No dead sensors found.")

    return dataframe

#Reads and cleans csv
canFrame = pd.read_csv('can_data.csv')
canFrame = cleandata(canFrame)

#RPM Graph
fig = px.line(canFrame, x='timestamp', y='RPM')
fig.show()

#TPS Graph
fig = px.line(canFrame, x='timestamp', y='TPS')
fig.show()
#Saves cleaned CSV
canFrame.to_csv("cleaned_can_data.csv", encoding='utf-8', index=False)