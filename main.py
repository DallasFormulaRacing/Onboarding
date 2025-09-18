import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def analyze_and_clean_can_data():
    
    
    #PART 1
    # load the data
    print("Loading CAN data...")
    df = pd.read_csv('/Users/tushaarsood/Documents/DFR/onboarding-project/Onboarding/can_data.csv')
    print(f"Loaded {len(df)} rows with {len(df.columns)} columns")
    
    # PART 2
    #Find and remove dead analog sensors
    
    # Get all analog columns
    analog_columns = [col for col in df.columns if 'Analog Input' in col]
    print(f"Found analog input columns: {analog_columns}")
    
    dead_sensors = []
    active_sensors = []
    
    for column in analog_columns:
        # remove null to analyze
        valid_data = df[column].dropna()
        
        if len(valid_data) == 0:
            # check for null senors off rip
            print(f"{column}: All null values → DEAD")
            dead_sensors.append(column)
            continue
        
        # Check if sensor has constant values/dead sensor
        unique_values = valid_data.nunique()
        variance = valid_data.var()
        
        print(f"{column}:")
        print(f"    Valid readings: {len(valid_data)}/{len(df)}")
        print(f"    Unique values: {unique_values}")
        print(f"    Range: {valid_data.min():.2f} to {valid_data.max():.2f}")
        print(f"    Variance: {variance:.6f}")
        
        # CHeck for dead sensors
        if variance < 0.001 or unique_values <= 2:
            print(f"  STATUS: DEAD (constant values/super low changes)")
            dead_sensors.append(column)
        else:
            print(f"    STATUS: ACTIVE")
            active_sensors.append(column)
    
    # Remove dead sensors from the dataframe
    print(f"\nRemoving {len(dead_sensors)} dead sensors: {dead_sensors}")
    df_cleaned = df.drop(columns=dead_sensors)
    print(f"Cleaned dataset now has {len(df_cleaned.columns)} columns left")
    
    #PART 3
    # RPM AND TPS GRAPHING
    print("\n---- RPM AND TPS dta -------------------")
    
    # RPM
    rpm_data = df_cleaned['RPM'].dropna()
    print(f"RPM: {len(rpm_data)} valid readings out of {len(df_cleaned)}")
    if len(rpm_data) > 0:
        print(f"RPM range: {rpm_data.min():.0f} - {rpm_data.max():.0f}")
    
    # TPS 
    tps_data = df_cleaned['TPS'].dropna()
    print(f"TPS: {len(tps_data)} / {len(df_cleaned)}")
    if len(tps_data) > 0:
        print(f"TPS range: {tps_data.min():.1f} - {tps_data.max():.1f}")
    
    # Create graphs
    print("\n-- MAKING GRAPHS ------------------")
    
    # Filter to rows that have both RPM and TPS data
    complete_data = df_cleaned.dropna(subset=['RPM', 'TPS', 'timestamp'])
    print(f"Found {len(complete_data)} rows with complete RPM and TPS data")
    
    if len(complete_data) > 0:
        # time fix
        complete_data['datetime'] = pd.to_datetime(complete_data['timestamp'], unit='s')
        
        # make plot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Engine RPM Over Time', 'Throttle Position (TPS) Over Time'),
            vertical_spacing=0.15
        )
        
        # Add rpm
        fig.add_trace(
            go.Scatter(
                x=complete_data['datetime'],
                y=complete_data['RPM'],
                mode='lines',
                name='RPM',
                line=dict(color='red', width=2)
            ),
            row=1, col=1
        )
        
        # Add TPS trace
        fig.add_trace(
            go.Scatter(
                x=complete_data['datetime'],
                y=complete_data['TPS'],
                mode='lines',
                name='TPS (%)',
                line=dict(color='blue', width=2)
            ),
            row=2, col=1
        )
        
        # Update layout
        fig.update_layout(
            title='CAN Data Metrics',
            height=600,
            showlegend=True
        )
        
        # Update y-axis labels
        fig.update_yaxes(title_text="RPM", row=1, col=1)
        fig.update_yaxes(title_text="TPS (%)", row=2, col=1)
        fig.update_xaxes(title_text="Time", row=2, col=1)
        
        # Show the graph
        fig.show()
        
    else:
        print("No complete data available for graphing!")
    
    return df_cleaned, dead_sensors, active_sensors

# Run the analysis
if __name__ == "__main__":
    cleaned_data, dead_sensors, active_sensors = analyze_and_clean_can_data()
    print("line executed")