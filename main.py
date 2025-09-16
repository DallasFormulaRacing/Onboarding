# DFR Onboarding 
# Shriya Shenoj

import pandas as pd
import plotly.express as px

# load CSV file
df = pd.read_csv('can_data (1).csv')

# make sure not all rows have same value (compare each cell of dataframe, column by column, to first row, and then locate those unidentical)
cleaned_df = df.loc[:, (df != df.iloc[0]).any()]
# remove empty columns (axis=1 points to columns and drop only columns with no values at all)
cleaned_df = cleaned_df.dropna(axis=1, how='all')

# check
print("Preview of cleaned data:")
print(cleaned_df.head())

# RPM over time
rpm_plot = px.line(cleaned_df, x="timestamp", y="RPM", title="RPM vs. Time")
rpm_plot.show()

# TPS over time
tps_plot = px.line(cleaned_df, x="timestamp", y="TPS", title="TPS vs. Time")
tps_plot.show()
