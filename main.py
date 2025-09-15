#Onboarding Project Submission
#Arjun Kaimal

#1 - load csv file
import pandas as pd
import plotly.express as plotx
df = pd.read_csv("can_data.csv")

#2 - clean data 
#drop cols w same values
cols_to_drop = [col for col in df.columns if df[col].nunique() == 1]
df_cleaned = df.drop(columns=cols_to_drop)
#drop cols w null
df_cleaned = df_cleaned.dropna(axis=1, how='all')

#3 and #4 - create line graphs
fig1 = plotx.line(df_cleaned, x="timestamp", y="RPM", title='RPM over Time Graph')
fig1.show()
fig2 = plotx.line(df_cleaned, x="timestamp", y="TPS", title='TPS over Time Graph')
fig2.show()