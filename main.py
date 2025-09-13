import pandas as pd
import plotly.express as px
import plotly.io as pio

# Force graphs to open in browser
pio.renderers.default = "browser"

# Loading the csv file
df = pd.read_csv("can-_ecu_762.csv")



# Removing columns where all sensors contain the same values
df = df.drop(columns=[col for col in df.columns if col.startswith("Analog Input")])

print(df.info())




# Plotting RPM and TPS vs Time graph
fig = px.line(df, x="timestamp", y=["RPM", "TPS"], title="RPM and TPS vs Time")
fig.show()