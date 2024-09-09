import pandas as pd
import plotly.graph_objects as go

# Load your CSV file
df = pd.read_csv('data.csv')

# Identify and remove constant Analog Input columns
analog_input_columns = [col for col in df.columns if 'Analog Input' in col]
non_constant_columns = [col for col in analog_input_columns if df[col].nunique() > 1]
df_filtered = df.drop(columns=[col for col in analog_input_columns if col not in non_constant_columns])

# Create a Plotly figure to plot RPM and TPS
fig = go.Figure()

# Check if 'RPM' and 'TPS' columns exist in the filtered dataframe
if 'RPM' in df_filtered.columns and 'TPS' in df_filtered.columns:
    # Plot RPM
    fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['RPM'], mode='lines', name='RPM'))

    # Plot TPS
    fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['TPS'], mode='lines', name='TPS'))

    # Update layout of the figure
    fig.update_layout(
        title='RPM and TPS Graphs',
        xaxis_title='Index',
        yaxis_title='Values',
        legend_title='Parameters'
    )

    # Show the plot
    fig.show()
else:
    print("RPM or TPS columns not found in the dataset.")
