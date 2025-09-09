import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def load_and_process_data():
    """Load CSV file and remove constant columns except Time"""
    # Load the CSV file
    df = pd.read_csv('can-_ecu_762.csv')
    
    # Rename timestamp column to Time for clarity
    df = df.rename(columns={'timestamp': 'Time'})
    
    # Remove constant columns (except Time)
    constant_columns = []
    for column in df.columns:
        if column != 'Time':
            # Check if column has any non-null values and if they're all the same
            non_null_values = df[column].dropna()
            if len(non_null_values) > 0 and non_null_values.nunique() <= 1:
                constant_columns.append(column)
    
    print(f"Removing {len(constant_columns)} constant columns: {constant_columns}")
    df = df.drop(columns=constant_columns)
    
    return df

def create_plots(df):
    """Create RPM and TPS plots using Plotly"""
    # Create subplots with 2 rows
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('RPM vs Time', 'TPS vs Time'),
        vertical_spacing=0.1
    )
    
    # Add RPM plot
    fig.add_trace(
        go.Scatter(
            x=df['Time'],
            y=df['RPM'],
            mode='lines',
            name='RPM',
            line=dict(color='blue')
        ),
        row=1, col=1
    )
    
    # Add TPS plot
    fig.add_trace(
        go.Scatter(
            x=df['Time'],
            y=df['TPS'],
            mode='lines',
            name='TPS',
            line=dict(color='red')
        ),
        row=2, col=1
    )
    
    # Update layout
    fig.update_layout(
        title='ECU Data Analysis - RPM and TPS vs Time',
        height=800,
        showlegend=True
    )
    
    # Update x-axis labels
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_xaxes(title_text="Time", row=2, col=1)
    
    # Update y-axis labels
    fig.update_yaxes(title_text="RPM", row=1, col=1)
    fig.update_yaxes(title_text="TPS", row=2, col=1)
    
    return fig

def main():
    """Main function to execute the analysis"""
    print("Loading and processing CSV data...")
    
    # Load and process data
    df = load_and_process_data()
    
    print(f"Data shape after processing: {df.shape}")
    print(f"Columns remaining: {list(df.columns)}")
    
    # Check if required columns exist
    if 'RPM' not in df.columns or 'TPS' not in df.columns:
        print("Error: Required columns 'RPM' or 'TPS' not found in data")
        return
    
    # Create and display plots
    print("Creating plots...")
    fig = create_plots(df)
    
    # Save the plots as HTML file
    fig.write_html("ecu_analysis_plots.html")
    print("Plots saved as 'ecu_analysis_plots.html'")
    print("Open this file in your web browser to view the interactive plots!")
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()