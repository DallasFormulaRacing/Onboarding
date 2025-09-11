import pandas as pd
import plotly.express as px
import plotly.io as pio

# Force graphs to open in browser
pio.renderers.default = "browser"

# Loading the csv file
df = pd.read_csv("can-_ecu_762.csv")



# Removing columns that contains null data
df = df.dropna(axis=1)


# Removing columns where all sensors contain the same values
df = df.loc[:, df.nunique() > 1]

print(df.info())

df = df.rename(columns={
    "timestamp": "Seconds",
    "Analog Input #1": "RPM",
    "Analog Input #2": "TPS"
})

df = df.dropna(axis=1)
df = df.loc[:, df.nunique() > 1]

print(df.info())


# Plotting RPM and TPS vs Time graph
fig = px.line(df, x="Seconds", y=["RPM", "TPS"], title="RPM and TPS vs Time")
fig.show()