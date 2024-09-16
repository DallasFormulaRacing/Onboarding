import pandas as pd
import plotly.express as px

filepath = '/Onboarding/dataDump.csv'
df = pd.read_csv(filepath, skiprows=1)

for col in df.columns:
    if df[col].nunique() == 1:  # Check if all values are the same
        df.drop([col], axis=1, inplace=True)

output_path = '/Onboarding/dataDumpNew.csv'
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
print(df)

x_column = 'RPM'
y_column = 'TPS'

fig = px.line(df, x=x_column, title=f'{x_column}')
fig.show()

fig = px.line(df, y=y_column, title=f'{y_column}')
fig.show()
print(f"Columns '{x_column}' or '{y_column}' not found in the DataFrame.")