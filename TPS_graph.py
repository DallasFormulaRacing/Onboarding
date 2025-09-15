import pandas as pd
import plotly.express as px

df = pd.read_csv('dfr_data.csv',header = None)
df.dropna()

dead_analog = [col for col in df if df[col].empty == True]
df = df.drop(columns=dead_analog)

fig = px.line(df, x=df[0], y=df[18], title="TPS over time", labels={"df[1]":"Time", "y":"TPS"}) 
fig.update_layout(autotypenumbers='convert types')
fig.show()