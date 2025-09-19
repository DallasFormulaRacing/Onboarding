import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def analyze_and_clean():
    # read file
    df = pd.read_csv('can_data.csv')
    # get all analog columns
    analog_columns = [col for col in df.columns if 'Analog Input' in col]
    
    dead_sensor=[]
    
    for column in analog_columns:
        # drop nan vals
        valid_data = df[column].dropna()
        
        if len(valid_data) == 0:
            dead_sensor.append(column)
            continue
    
    df_live = df.drop(columns= dead_sensor) # gettting rid of sensors that are dead
    
    df_complete = df_live.dropna(subset = ['RPM', 'TPS', 'timestamp']) # for specific drops
    
    if len(df_complete) > 0:
        df_complete['datetime'] = pd.to_datetime(df_complete['timestamp'], unit='s') # datetime conversion
        
        #make the base of plot
        fig = make_subplots(
            rows= 2, cols = 1,
            subplot_titles = ['RPM over time', 'TPS over time'],
            vertical_spacing = 0.15
        )
        # add the rmp
        fig.add_trace(
            go.Scatter(
                x = df_complete['datetime'],
                y = df_complete['RPM'],
                mode = 'lines',
                name='RPM',
                line=dict(color='red')
            ),
            row = 1, col = 1
        )
        # add the tps
        fig.add_trace(
            go.Scatter(
                x = df_complete['datetime'],
                y = df_complete['TPS'],
                mode = 'lines',
                name='TPS',
                line=dict(color='blue')
            ),
            row = 2, col = 1
        )
        
        fig.show()
        return df_live, dead_sensor
    
    
if __name__ == "__main__":
    df_new, dead_sensors = analyze_and_clean()