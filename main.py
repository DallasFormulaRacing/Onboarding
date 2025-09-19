import pandas as pd
import plotly.express as px

#Load CSV
csv_file = "can_data.csv" 
df = pd.read_csv(csv_file)

#Remove 'Analog Input' w columns same value
for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df.drop(col, axis=1, inplace=True)

#Plot RPM over time
if 'RPM' in df.columns:
    fig_rpm = px.line(
        df,
        x='timestamp',
        y='RPM',
        title='RPM over Time',
        labels={'timestamp': 'Time', 'RPM': 'RPM'}
    )
    fig_rpm.show()

#Plot TPS over time
if 'TPS' in df.columns:
    fig_tps = px.line(
        df,
        x='timestamp',
        y='TPS',
        title='TPS over Time',
        labels={'timestamp': 'Time', 'TPS': 'TPS'}
    )
    fig_tps.show()




