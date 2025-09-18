print("hello world my changes")

import pandas as pd

df = pd.read_csv("can_data.csv")

# Find all 'Analog Input' columns
analog_cols = [col for col in df.columns if col.startswith("Analog Input")]

# Keep only those that actually change (more than 1 unique value)
changing_analog_cols = [col for col in analog_cols if df[col].nunique(dropna=True) > 1]

# Rebuild dataframe: keep everything except dead Analog Inputs
df = df.drop(columns=[col for col in analog_cols if col not in changing_analog_cols])

print("Removed Analog Input columns:",
      [col for col in analog_cols if col not in changing_analog_cols])
print("Kept Analog Input columns:", changing_analog_cols)

# Save cleaned data if needed
df.to_csv("can_data_cleaned.csv", index=False)