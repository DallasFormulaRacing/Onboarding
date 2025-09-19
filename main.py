import plotly.express as px
import pandas as pd 
import math

df = pd.read_csv('can_data.csv')

new_df = None

ANALOG_INPUT_TEXT='Analog Input #'
columns = df.columns.tolist()

for sensor in columns:
    if sensor.startswith(ANALOG_INPUT_TEXT):
        unique_values = df[sensor].unique()
        filtered_list = [s for s in unique_values if not math.isnan(s)]
        count = len(filtered_list)
        print(f"Sensor {sensor}: {count}")
        #if number of unique sensors value is 1, then it is dead and will be removed
        if count == 1:
            print("####################################")
            print("Removing dead sensor "+ sensor)
            print("####################################")
            new_df = df.drop(sensor, axis=1)

print(new_df)

#Code for Plotly graphs
RPMfig = px.line(new_df, x="timestamp", y="RPM", title="Change in RPM Over Time", color_discrete_sequence=['purple'])
RPMfig.update_layout(title_x=0.5)
RPMfig.show()

TPSfig = px.line(new_df, x="timestamp", y="TPS", title="Change in TPS Over Time", template='plotly_dark')
TPSfig.update_layout(title_x=0.5)
TPSfig.show()

#I messed around with the colors and themes a bit just for fun

