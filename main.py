import plotly.express as px
import pandas as pd 

df = pd.read_csv('can_data.csv')

MAX_SENSORS=7
new_df = None

ANALOG_INPUT_TEXT='Analog Input #'

for sensor in range(1, MAX_SENSORS+1):
    count = len(df[ANALOG_INPUT_TEXT + str(sensor)].unique())
    
    if count == 1:
        print("####################################")
        print("Removing dead sensor #"+str(sensor))
        print("####################################")
        new_df = df.drop(ANALOG_INPUT_TEXT + str(sensor), axis=1)

print(new_df)

#Code for Plotly graphs
RPMfig = px.line(new_df, x="timestamp", y="RPM", title="Change in RPM Over Time", color_discrete_sequence=['purple'])
RPMfig.update_layout(title_x=0.5)
RPMfig.show()

TPSfig = px.line(new_df, x="timestamp", y="TPS", title="Change in TPS Over Time", template='plotly_dark')
TPSfig.update_layout(title_x=0.5)
TPSfig.show()

#I messed around with the colors and themes a bit just for fun

