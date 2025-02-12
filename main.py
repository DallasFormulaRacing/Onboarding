import pandas as pd
import plotly.express as px
import numpy as np




csv_File = "DiscordData.csv"
dataDump = pd.read_csv(csv_File)


analog_data = [col for col in dataDump.columns if 'Analog Input' in col]
constant_data = [col for col in analog_data if dataDump[col].nunique() == 1]


dataDump_Clean = dataDump.drop(columns = constant_data)
dataDump_Clean.to_csv("Modified_Data_File.csv", index = False)


time = dataDump_Clean['timestamp'].values


if 'RPM' in dataDump_Clean.columns and 'TPS' in dataDump_Clean.columns and 'timestamp' in dataDump_Clean.columns:
    dataDump_Clean['timestamp'] = pd.to_datetime(dataDump_Clean['timestamp'])
   
    fig_RPM = px.line(dataDump_Clean,x = time, y = 'RPM', title = "RPM Over Time")
    fig_RPM.update_xaxes(title_text="Time")
    fig_RPM.show()


    fig_TPS = px.line(dataDump_Clean, x = time, y = 'TPS', title = "TPS Over Time")
    fig_TPS.update_xaxes(title_text="Time")
    fig_TPS.show()
else:
    print("The columns of RPM and TPS were not found")





