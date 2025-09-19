import pandas as pd
import plotly.express as px

df = pd.read_csv("can_data.csv")

for col in df.columns:
  if "Analog Input" in col and df[col].nunique() ==1:
    df.drop(col, axis = 1, inplace = True)

fig_rpm = px.line(df, x = "timestamp", y = "RPM", title = "RPM over Time")
fig_rpm.update_xaxes(title = "Timestamp")
fig_rpm.update_yaxes(title = "RPM")
fig_rpm.show()

fig_tps = px.line(df, x = "timestamp", y = "TPS", title = "TPS over Time")
fig_tps.update_xaxes(title = "Timestamp")
fig_tps.update_yaxes(title = "Throttle Position Sensor(TPS)")
fig_tps.show()

