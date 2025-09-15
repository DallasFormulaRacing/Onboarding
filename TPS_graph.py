import pandas as pd
import plotly.express as px

df = pd.read_csv('dfr_data.csv',header = None)
df.dropna().head()

dead_analog = [col for col in df if df[col].empty == True]
df = df.drop(columns=dead_analog)

fig = px.line(df, x=df[0], y=df[18], title="RPM over time", labels={"x":"Time", "y":"RPM"}) 
fig.update_layout(autotypenumbers='convert types')
fig.show()