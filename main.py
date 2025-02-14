import pandas as pd
import plotly.express as px

#load data from the CSV file

csv_file = "graphData.csv"
data = pd.read_csv(csv_file)

#filter out columns containing 'Analog Input' with constant values

analog_columns = [col for col in data.columns if 'Analog Input' in col]
constant_columns = [col for col in analog_columns if data[col].nunique() == 1]
data_cleaned = data.drop(columns=constant_columns)

#save cleaned data to a new CSV file

data_cleaned.to_csv("graphDataUpdated.csv", index=False)

#extract the time column for plotting

if 'timestamp' in data_cleaned.columns:
    time = data_cleaned['timestamp']

    #check for required columns before plotting
    
    if {'RPM', 'TPS'}.issubset(data_cleaned.columns):
        #RPM over time
        
        fig_rpm = px.line(data_cleaned, x=time, y='RPM', title="RPM Over Time")
        fig_rpm.update_xaxes(title_text="Time")
        fig_rpm.show()

        #TPS over time
        
        fig_tps = px.line(data_cleaned, x=time, y='TPS', title="TPS Over Time")
        fig_tps.update_xaxes(title_text="Time")
        fig_tps.show()
     
     #RPM and TPS not found in data
        
    else:
        print("Required columns 'RPM' and 'TPS' are not found in the data.")

#timestamp not found in data

else:
    print("Column 'timestamp' is missing from the data.")