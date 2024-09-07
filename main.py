import pandas as pd
import plotly.express as px

# Load the CSV file
file_name = 'can-_ecu_762.csv'
try:
    df = pd.read_csv(file_name)
    print(f"Successfully loaded {file_name}.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
    exit()

# Check if 'RPM' and 'TPS' columns exist in the data
required_columns = ['RPM', 'TPS']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Error: Missing columns: {', '.join(missing_columns)}. Please check the data file.")
    exit()

# Remove columns that have the same value throughout
df = df.loc[:, df.nunique() > 1]

# Check if the DataFrame still has the required data
if df.empty:
    print("Error: All columns were removed. No data to plot.")
    exit()

# Plot RPM
if 'RPM' in df.columns:
    fig_rpm = px.line(df, x='timestamp', y='RPM', title='RPM over Time')
    fig_rpm.show()
else:
    print("Warning: 'RPM' column not found after cleaning data.")

# Plot TPS
if 'TPS' in df.columns:
    fig_tps = px.line(df, x='timestamp', y='TPS', title='TPS over Time')
    fig_tps.show()
else:
    print("Warning: 'TPS' column not found after cleaning data.")
