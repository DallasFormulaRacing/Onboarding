import pandas as pd 
import plotly.express as px 


dataFile = pd.read_csv(r"C:\Users\JN\Desktop\Onboarding\can-_ecu_762.csv") # read data dump file

analogInputsRead = [columnName for columnName in dataFile.columns if 'Analog Input' in columnName] # create list of columns with names that include Analog input


dataFileCleaned = dataFile.drop(columns=[columnName for columnName in analogInputsRead if dataFile[columnName].nunique() == 1]) # drop any columns that have only 1 unique element


graphRPM = px.line(dataFileCleaned, x='timestamp', y='RPM', title='RPM VS Time', labels={
        'timestamp': 'Time',
        'RPM': 'Engine RPM'}).show()
graphTPS = px.line(dataFileCleaned, x='timestamp', y='TPS', title='TPS VS Time', labels={
        'timestamp': 'Time',
        'TPS': 'Throttle Position (%)'
    }).show()
