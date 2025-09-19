import pandas as pd
import plotly.graph_objects as plot

df = pd.read_csv('can_data.csv')

# Drops analog input columns whose value does not change
TOLERANCE = 0.001
dead_cols = [
    c for c in df.columns
    if c.startswith("Analog Input") and (df[c].max() - df[c].min()) < TOLERANCE
]
df.drop(columns=dead_cols, inplace=True)
print("Dropped columns:", dead_cols)

cleanedCSV = "cleaned_can_data.csv"
df.to_csv("cleaned_can_data.csv", index=False)

# Setting column names from the csv file
time_col = 'timestamp'
rpm_col = 'RPM'
tps_col = 'TPS'

# Creating plots
# RPM plot
fig_rpm = plot.Figure()
fig_rpm.add_trace(plot.Scatter(x=df[time_col], y=df[rpm_col], mode="lines", name="RPM"))
fig_rpm.update_layout(title="RPM Over Time", xaxis_title="Time", yaxis_title="RPM")
fig_rpm.show()

# TPS plot
fig_tps = plot.Figure()
fig_tps.add_trace(plot.Scatter(x=df[time_col], y=df[tps_col], mode="lines", name="TPS", line=dict(color="red")))
fig_tps.update_layout(title="TPS Over Time", xaxis_title="Time", yaxis_title="TPS")
fig_tps.show()