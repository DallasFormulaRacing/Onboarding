import pandas as pd
import plotly.express as px
import webbrowser

# 1 open csvgit add main.py

df = pd.read_csv("can_data.csv")

# 2 clean data
for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df = df.drop(columns=[col])
print(df)

#3-RMP graph
fig_rpm = px.line(
    df, x="timestamp", y="RPM",
    title="RPM Over Time",
    labels={"timestamp": "Timestamp", "RPM": "Engine RPM"}
)
#4-TPS graph
fig_tps = px.line(
    df, x="timestamp", y="TPS",
    title="TPS Over Time",
    labels={"timestamp": "Timestamp", "TPS": "Throttle Position"}
)
#html
fig_rpm.write_html("rpm_over_time.html")
fig_tps.write_html("tps_over_time.html")
#open in browser
fig_rpm.show()
fig_tps.show()
