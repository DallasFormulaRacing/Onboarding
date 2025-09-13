import pandas
import plotly.express

# Read CSV into a Pandas DF
df = pandas.read_csv('can-_ecu_762.csv')

# Drop columns with null and/or repeated sensor data
df = df.dropna(axis = 1, how = "all")
df = df.loc[:, df.nunique(dropna = True) > 1]

# Create graph with Plotly to show change in RMP and TPS over time
df = df.reset_index().rename(columns={"index": "Time (samples)"})

plotly.express.line(df, x="Time (samples)", y="RPM", title="RPM over Samples").show()
plotly.express.line(df, x="Time (samples)", y="TPS", title="TPS over Samples").show()
