import pandas as pd
import plotly.express as px


df = pd.read_csv("can_data.csv")


for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df.drop(columns=[col], inplace=True)


fig1 = px.line(
    df,
    x="timestamp",   
    y="RPM",
    title="RPM Over Time",
    labels={"timestamp": "Timestamp", "RPM": "Revolutions per Minute"}
)


fig2 = px.line(
    df,
    x="timestamp",   
    y="TPS",
    title="TPS Over Time",
    labels={"timestamp": "Timestamp", "TPS": "Throttle Position Sensor"}
)

fig1.show()
fig2.show()