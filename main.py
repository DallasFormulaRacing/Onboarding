import pandas as pd
import plotly.express as px

df = pd.read_csv("can_data.csv")

keep = {"timestamp", "RPM", "TPS"}

#clean data remove null and same vals
null_cols = [c for c in df.columns if c not in keep and df[c].isna().any()]
df = df.drop(columns=null_cols)
const_cols = [c for c in df.columns if c not in keep and df[c].nunique(dropna=False) <= 1]
df = df.drop(columns=const_cols)

#convert timestamp to seconds
df["time_s"] = df["timestamp"] - df["timestamp"].min()

#keep only rows with values in key columns
df_plot = df.dropna(subset=["timestamp", "RPM", "TPS"]).copy()

#RPM graph
rpm_graph = px.line(df_plot, x="time_s", y="RPM",
                  title="Engine RPM over Time",
                  labels={"time_s": "Time (s)", "RPM": "RPM"})
rpm_graph.write_html("rpm_graph.html", include_plotlyjs="cdn")

#TPS graph
tps_graph = px.line(df_plot, x="time_s", y="TPS",
                  title="Throttle Position (TPS) over Time",
                  labels={"time_s": "Time (s)", "TPS": "TPS (%)"})
tps_graph.write_html("tps_graph.html", include_plotlyjs="cdn")

#combined graph
long_df = df_plot[["time_s", "RPM", "TPS"]].melt(
    id_vars=["time_s"], var_name="Signal", value_name="Value"
)
combined_graph = px.line(long_df, x="time_s", y="Value", color="Signal",
                       title="RPM & TPS over Time",
                       labels={"time_s": "Time (s)", "Value": "Value"})
combined_graph.write_html("combined_graph.html", include_plotlyjs="cdn")
