import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("can-_ecu_762.csv")
1
for col in df.columns:
    if 'Analog Input' in col and df[col].nunique() == 1:
            df.drop(columns=col, inplace=True)
            print(f"Removed constant columns: {col}")


fig = make_subplots(rows=2, cols=1)

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['RPM'], name="RPM/Time"), 
    row=1, col=1
    )

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['TPS'], name="TPS/Time"), 
    row=2, col=1
    )

fig.update_layout(title_text="RPM and TPS Over Time")

fig.show()