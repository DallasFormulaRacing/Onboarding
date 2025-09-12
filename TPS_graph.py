import pandas as pd
import plotly.express as px

df = pd.read_csv('dfr_data.csv',header = None)
#df.dropna(inplace=True)
df.head()

#t = df[0]
#print(t)
#print(df.to_string()) 
#df = px.data.gapminder().query("run=='Run #1'")
#fig = px.line(df, x="timestamp", y="RMP", title='RPM over time')
#fig.show()

fig = px.line(df, x=df[0], y=df[18], title="RPM over time") 
fig.update_layout(autotypenumbers='convert types')
fig.show()