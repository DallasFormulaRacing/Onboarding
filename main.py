# DFR Onboarding Project
# Akshaj Ande

import pandas as pd
import plotly.express as px

# Reading CSV into Pandas DataFrame
df = pd.read_csv("can_data.csv")

# Removing columns with only one unique value and dropping fully empty columns
df_clean = df[[c for c in df.columns if df[c].nunique() > 1]].dropna(axis=1, how="all")

# Creating Graphs
rpm_graph = px.line(
    df_clean, 
    x="timestamp", 
    y="RPM", 
    labels={"timestamp": "Time", "RPM": "RPM"},
    title="RPM vs Time"
)

tps_graph = px.line(
    df_clean, 
    x="timestamp", 
    y="TPS", 
    labels={"timestamp": "Time", "TPS": "TPS"},
    title="TPS vs Time"
)

# Showing Graphs
rpm_graph.show()
tps_graph.show()
