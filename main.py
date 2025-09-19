from narwhals import col
import pandas
import plotly

DataFrame = pandas.read_csv("can_data.csv")


for col in DataFrame.columns:
    if "Analog Input" in col and DataFrame[col].nunique() == 1:
        DataFrame = DataFrame.drop(columns=[col])
        print(f"Dropped column: {col}")
        

#RPM Plot
import plotly.graph_objects as go
fig_rpm = go.Figure()
fig_rpm.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['RPM'], mode='lines', name='RPM', line=dict(color='red')))
fig_rpm.update_layout(
    title='Engine RPM Over Time',
    xaxis_title='Timestamp (seconds)',
    yaxis_title='RPM',
    font=dict(size=14),
    plot_bgcolor='white'
)
fig_rpm.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig_rpm.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig_rpm.show()

# TPS Plot
fig_tps = go.Figure()
fig_tps.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['TPS'], mode='lines', name='TPS', line=dict(color='blue')))
fig_tps.update_layout(
    title='Throttle Position Sensor (TPS) Over Time',
    xaxis_title='Timestamp (seconds)',
    yaxis_title='TPS',
    font=dict(size=14),
    plot_bgcolor='white'
)
fig_tps.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig_tps.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig_tps.show()