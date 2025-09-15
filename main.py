# DFR Onboarding 
# Shriya Shenoj

import pandas as pd
import plotly.express as px

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('can_data (1).csv')

# Step 2: Remove columns that are constant or completely empty
# Keep columns where at least one value differs from the first row
cleaned_df = df.loc[:, (df != df.iloc[0]).any()]
# Drop columns that are fully null
cleaned_df = cleaned_df.dropna(axis=1, how='all')

# Optional: print the first few rows to verify cleaning
print("Preview of cleaned data:")
print(cleaned_df.head())

# Step 3: Plot RPM over time
rpm_plot = px.line(cleaned_df, x="timestamp", y="RPM", title="RPM vs. Time")
rpm_plot.show()

# Step 4: Plot TPS over time
tps_plot = px.line(cleaned_df, x="timestamp", y="TPS", title="TPS vs. Time", color_discrete_sequence=['red'])
tps_plot.show()
