import pandas as pd
import plotly.express as px

# read data to df
df = pd.read_csv('can_data.csv')

# drop Analog Input columns with nulls
analog_cols = [col for col in df.columns if col.startswith("Analog Input")]

# Drop analog input columns with any NaN
df = df.drop(columns=[col for col in analog_cols if df[col].isna().any()])

print(df)

fig_RPM = px.line(df, x="timestamp", y="RPM", title='RPM over Time')
fig_RPM.show()

fig_TPS = px.line(df, x="timestamp", y="TPS", title='TPS over Time')
fig_TPS.show()