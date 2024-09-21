import pandas as pd
import plotly.express as px

# load csv file
data = pd.read_csv('can-_ecu_762.csv')

# clean out analog input columns that have same value throughout
analogInputs = [col for col in data.columns if "Analog Input" in col]
cleanedData = data.drop(columns=[col for col in analogInputs if data[col].nunique() == 1])

# check if RPM and TPS columns exist and plot them if they do
if 'RPM' in cleanedData.columns and 'TPS' in cleanedData.columns:
    graphRPM = px.line(cleanedData, x='timestamp', y='RPM', title='RPM vs Time')
    graphTPS = px.line(cleanedData, x='timestamp', y='TPS', title='TPS vs Time')
    graphRPM.show()
    graphTPS.show()
else:
    print("Error: RPM or TPS not found in cleaned data.")