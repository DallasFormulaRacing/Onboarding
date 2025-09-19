import pandas as pd
import plotly.express as px
from pathlib import Path

# 1) Load CSV
df = pd.read_csv("can_data.csv")

# 2) Drop constant "Analog Input" columns
dead_sensors = [col for col in df.columns if "Analog Input" in col and df[col].nunique(dropna=False) == 1]
df.drop(columns=dead_sensors, inplace=True)
print(f"Removed dead sensors: {dead_sensors}")

# 3) Make sure rows are sorted by timestamp
df = df.sort_values(by="timestamp")

# 4) Create output folder
Path("output").mkdir(exist_ok=True)

# 5) Plot RPM
fig_rpm = px.line(
    df, x="timestamp", y="RPM",
    title="RPM over Time",
    labels={"timestamp": "Timestamp", "RPM": "Revolutions per Minute"}
)
fig_rpm.write_html("output/rpm_over_time.html", auto_open=True)

# 6) Plot TPS
fig_tps = px.line(
    df, x="timestamp", y="TPS",
    title="TPS over Time",
    labels={"timestamp": "Timestamp", "TPS": "Throttle Position (%)"}
)
fig_tps.write_html("output/tps_over_time.html", auto_open=True)

print("Charts saved in 'output/' folder.")
