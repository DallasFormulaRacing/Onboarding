import pandas as pd
import plotly.express as px

#load the CSV into a pandas DataFrame
df = pd.read_csv('can_data.csv')


print("Columns before cleaning:")
print(df.columns)


#removing 'Analog Input' 
for col in df.columns:
    if 'Analog Input' in col and df[col].nunique() == 1:
        df.drop(col, axis=1, inplace=True)


# RPM graph
fig_rpm = px.line(
    df,
    x='timestamp',  # use lowercase as in your CSV
    y='RPM',
    title='RPM vs Time',
    labels={'RPM': 'Engine RPM', 'timestamp': 'Time (s)'}
)
fig_rpm.show()


# TPS graph
fig_tps = px.line(
    df,
    x='timestamp',  # use lowercase as in your CSV
    y='TPS',
    title='TPS vs Time',
    labels={'TPS': 'Throttle Position', 'timestamp': 'Time (s)'}
)
fig_tps.show()

