import pandas as pd
import plotly.express as px

#load csv
df = pd.read_csv("can_data.csv")

#remove 'Analog Input' columns that never change
for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df = df.drop(columns=[col])

print("Columns after cleaning:")
print(df.columns)

#plot RPM over time
if "RPM" in df.columns:
    fig_rpm = px.line(df, x="timestamp", y="RPM", title="RPM over Time")
    fig_rpm.show()
else:
    print(" RPM column not found")

#plot tps over time
if "TPS" in df.columns:
    fig_tps = px.line(df, x="timestamp", y="TPS", title="TPS over Time")
    fig_tps.show()
else:
    print(" TPS column not found")
