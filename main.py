import pandas
import plotly

# Read CSV into a Pandas DF
df = pandas.read_csv('can-_ecu_762.csv')

print(df.head)

# Remove null and non-working sensor data

# Create graph with Plotly to show change in RMP and TPS over time

