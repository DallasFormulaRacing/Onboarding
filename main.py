import pandas as pd
import plotly.express as px

#1. Load the CSV file into a pandas DataFrame.

df = pd.read_csv("can_data.csv")

#2. Clean the data by removing all columns named 'Analog Input' that contain the same value for every row.

df = df.drop(columns = [col for col in df.columns if 'Analog Input' in col and df[col].nunique() == 1])

#3. Create a line graph(s) using plotly that shows the change in RPM over time and change in TPS over time. This can either be done in separate graphs or in the same graph if you prefer.

rpm = px.line(df, x = "timestamp", y = "RPM", title = "RPM vs. Time")
tps = px.line(df, x = "timestamp", y = "TPS", title = "TPS vs. Time")

#4. Add appropriate titles and labels to your graphs for clarity.

rpm.show()
tps.show()