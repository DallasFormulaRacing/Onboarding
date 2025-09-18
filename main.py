print("hello world my changes")

import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"



df = pd.read_csv("can_data.csv")


# Find all 'Analog Input' columns
analog_cols = [col for col in df.columns if col.startswith("Analog Input")]

# Keep only those that actually change (more than 1 unique value)
changing_analog_cols = [col for col in analog_cols if df[col].nunique(dropna=True) > 1]

# Rebuild dataframe: keep everything except dead Analog Inputs
df = df.drop(columns=[col for col in analog_cols if col not in changing_analog_cols])

print("Removed Analog Input columns:",
      [col for col in analog_cols if col not in changing_analog_cols])
print("Kept Analog Input columns:", changing_analog_cols)

# Save cleaned data if needed
df.to_csv("can_data_cleaned.csv", index=False)


# Convert timestamp if it's numeric (seconds since epoch)
if pd.api.types.is_numeric_dtype(df["timestamp"]):
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")

# RPM graph with title and labels
fig_rpm = px.line(
    df, x="timestamp", y="RPM",
    title="Engine RPM Over Time",
    labels={"timestamp": "Time", "RPM": "Revolutions Per Minute"}
)
fig_rpm.show()

# TPS graph with title and labels
fig_tps = px.line(
    df, x="timestamp", y="TPS",
    title="Throttle Position Over Time",
    labels={"timestamp": "Time", "TPS": "Throttle Position Sensor (%)"}
)
fig_tps.show()