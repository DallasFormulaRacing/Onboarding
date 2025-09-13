import pandas
import plotly

# Read CSV into a Pandas DF
df = pandas.read_csv('can-_ecu_762.csv')

# Remove null and non-working sensor data
df = df.dropna(axis = 1, how = all)
df = df.loc[:, df.nunique(dropna = True) > 1]

# Create graph with Plotly to show change in RMP and TPS over time
