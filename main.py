import pandas as pd
import plotly.express as px

df = pd.read_csv("can_data.csv")

dead_sensors = [col for col in df.columns if "Analog Input" in col and df[col].nunique() == 1]
df.drop(columns=dead_sensors, inplace=True)

print(f"Removed dead sensors: {dead_sensors}")
print("Remaining columns:", df.columns.tolist())

rpm = px.line(
    df, 
    x="timestamp", 
    y="RPM",
    title="Change in RPM over Time",
    labels={"timestamp": "Timestamp", "RPM": "Revolutions per Minute"}
)
rpm.show()

tps = px.line(
    df, 
    x="timestamp", 
    y="TPS",
    title="Change in TPS over Time",
    labels={"timestamp": "Timestamp", "TPS": "Throttle Position (%)"}
)
tps.show()
