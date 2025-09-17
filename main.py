import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read csv
df = pd.read_csv('can-_ecu_762.csv')

# Drop 'Analog Input' columns with constant values
df = df.drop(
    columns=[col for col in df.columns
        if 'Analog Input' in col and df[col].nunique(dropna=True) == 1
    ]
)

print(df.info())

# Graph RPM and TPS vs Time
fig = make_subplots(rows=1, cols=2, subplot_titles=('RPM vs Time', 'TPS vs Time'))

# RPM vs Time
fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['RPM']),
    row=1, col=1
)
fig.update_xaxes(title_text='Time', row=1, col=1)
fig.update_yaxes(title_text='RPM', row=1, col=1)

# TPS vs Time
fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['TPS']),
    row=1, col=2
)
fig.update_xaxes(title_text='Time', row=1, col=2)
fig.update_yaxes(title_text='TPS', row=1, col=2)

fig.update_layout(title_text='RPM and TPS vs Time')
fig.show()
