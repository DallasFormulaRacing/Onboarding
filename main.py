import plotly
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# store data in a data frame
data = pd.read_csv("can-_ecu_762.csv")

# determine which columns do not change (have only 1 unique value)
print("Analog Input #1: ")
print(data['Analog Input #1'].unique())
print("Analog Input #2: ")
print(data['Analog Input #2'].unique())
print("Analog Input #3: ")
print(data['Analog Input #3'].unique())
print("Analog Input #4: ")
print(data['Analog Input #4'].unique())
print("Analog Input #5: ")
print(data['Analog Input #5'].unique())
print("Analog Input #6: ")
print(data['Analog Input #6'].unique())
print("Analog Input #7: ")
print(data['Analog Input #7'].unique())
print("Analog Input #8: ")
print(data['Analog Input #8'].unique())

# drop columns which do not change
data.drop(["Analog Input #3", "Analog Input #5", "Analog Input #7", "Analog Input #8"], axis=1, inplace=True)

# display data in tabular format
print(data)

time = data['timestamp'].values
rpm = data['RPM'].values
tps = data['TPS'].values

# Create a figure
fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()

# Add RPM trace
fig1.add_trace(go.Scatter(x=time, y=rpm, mode='lines', name='RPM'))

# Add TPS trace with a secondary y-axis
fig2.add_trace(go.Scatter(x=time, y=tps, mode='lines', name='TPS'))

fig3.add_trace(go.Scatter(x=time, y=rpm, mode='lines', name='RPM', yaxis='y1'))
fig3.add_trace(go.Scatter(x=time, y=tps, mode='lines', name='TPS', yaxis='y2'))

fig1.update_layout(title='Time vs RPM', xaxis_title='Time', yaxis_title='RPM')
fig2.update_layout(title='Time vs TPS', xaxis_title='Time', yaxis_title='TPS')
# Create layout with two y-axes
fig3.update_layout(title='Time vs RPM and TPS', xaxis_title='Time', yaxis_title='RPM', yaxis2=dict(title='TPS', overlaying='y', side='right'), legend=dict(x=0, y=1.0))

pyo.plot(fig1, filename='line_graph_1.html', auto_open=True)
pyo.plot(fig2, filename='line_graph_2.html', auto_open=True)
pyo.plot(fig3, filename='line_graph_3.html', auto_open=True)