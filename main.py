import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser" #opens the grpahs on a new tab on the browser

df = pd.read_csv('can_data.csv')

for col in df.columns:
    if col.startswith("Analog Input") and df[col].nunique() <= 1:
        df = df.drop(columns=[col])

fig = px.line(df, x='timestamp', y='RPM', title='Change In RPM Over Time')
fig_2 = px.line(df, x='timestamp', y='TPS', title='Change In TPS Over Time')
fig.update_layout(xaxis_title="Time", yaxis_title="RPM")
fig_2.update_layout(xaxis_title="Time", yaxis_title="TPS (%)")
fig.show()
fig_2.show()