import pandas as pd
import plotly.express as px

df = pd.read.csv(can_data.csv)

for col in df.columns:
  if "Analog Input" in col and df[col].nunique() ==1:
    df.drop(col, axis = 1, inplace = true)

fig_rpm = px.line(df, x = "Time", y = "RPM", title = "RPM over Time")
fig_rpm.update_xaxes(title = "Time")
fig_rpm.update_yaxes(title = "RPM")
fig_rpm.show()

fig_tps = px.line(df, x = "Time", y = "TPS", title = "TPS over Time")
fi_tps.update_xaxes(title = "Time")
fig_tps.update_yaxes(title = "Throttle position Seonsor(TPS)")
fig_tps.show()

