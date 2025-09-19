import pandas as pd
import plotly.express as px

df = pd.read_csv('can_data.csv')
print(df.head())

inputs = [ col for col in df.columns if 'Analog Input' in col]

drop_cols = []
# go through each column
for col in inputs:
    if df[col].nunique() == 1: # number of unique values is only 1 
        drop_cols.append(col)

# cleaned data frame 
df_clean = df.drop(columns=drop_cols)

# debug
if drop_cols:
    print(f"removed these columns: {drop_cols}")
else:
    print("all columns are unique")

# printing graph
graph = px.line(df_clean, x='timestamp', y=['RPM', 'TPS'],
                title="RPM vs TPS",
                labels={'value': 'Value', 'timestamp': 'Timestamp', 'variable': 'Metric'})\
                
graph.write_html("rpm_tps_plot.html")
graph.write_image("rpm_tps_plot.png", scale=2)
graph.show()
