import pandas as pd
import plotly.express as px

df = pd.read_csv('dfr_data.csv',header = None)
df.head()

fig = px.line(df, x=df[0], y=df[18], title="RPM over time") 
fig.update_layout(autotypenumbers='convert types')
fig.show()
