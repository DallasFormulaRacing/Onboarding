import pandas as pd
import plotly.express as px

file_path = 'can-_ecu_762.csv'  
df = pd.read_csv(file_path)


columns_to_drop = []
for col in df.columns:
    if df[col].nunique() == 1:
        columns_to_drop.append(col)

df_cleaned = df.drop(columns=columns_to_drop)


rpm_column = []
tps_column = []
for col in df_cleaned.columns:
    if 'RPM' in col:
        rpm_column.append(col)
    if 'TPS' in col:
        tps_column.append(col)


if rpm_column and tps_column:
    fig_rpm = px.line(df_cleaned, x='timestamp', y=rpm_column[0], title='RPM Over Time')
    fig_rpm.show()

    fig_tps = px.line(df_cleaned, x='timestamp', y=tps_column[0], title='TPS Over Time')
    fig_tps.show()
else:
    print("Missing columns:")
    if not rpm_column: print("RPM column not found.")
    if not tps_column: print("TPS column not found.")
