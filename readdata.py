
#troubleshooting code
#import os
#print("Current working directory:", os.getcwd())

import pandas as pd
import plotly.express as px

df = pd.read_csv("can_data.csv")

for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df.drop(columns=[col], inplace=True)

print(df.head())

#RPM over time graph
fig_rpm = px.line(df, x = "timestamp", y = "RPM", title = "RPM Over Time")
fig_rpm.update_layout(xaxis_title="Time (seconds)")
fig_rpm.show()

#TPS over time graph
fig_TPS = px.line(df, x = "timestamp", y = "TPS", title = "TPS Over Time")
fig_TPS.update_layout(xaxis_title="Time (seconds)")
fig_TPS.show()

