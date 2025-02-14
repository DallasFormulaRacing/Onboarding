#using our necessary imports from plotly and pandas
import plotly.express as px
import pandas as pd

df = pd.read_csv('can-_ecu_762.csv') #reads csv file
df = df.loc[:, df.nunique() != 1] #line to ignore and repeated analog inputs

if 'RPM' in df.columns and 'TPS' in df.columns:
    #Using the line graph from plotly
    fig = px.line(
        df, 
        x = df.index, # gets the index from the x axis which will be time/sample
        y = ['RPM', 'TPS'], #name for each line
        title = 'RPM/TPS graph', #main title
        labels = {'value': 'Value', 'variable': 'Line'}, #labels to hold the value and name of the RPM or TPS
    )

    #makes the x and y axis titles and allows the user to hover over the graph and show the data at the specific points
    fig.update_layout(xaxis_title ='Time and Samples', yaxis_title = 'Value', hovermode = 'x unified')

    fig.update_traces(selector = {'name': 'RPM'}, line_color = '#82C8F6') #changes the RPM line color to a light blue
    fig.update_traces(selector = {'name': 'TPS'}, line_color = '#98D8AF') #changes the RPM line color to a light green
    fig.show()

else:
    #in case of error where the RPM or TPS doesn't show, it will print this statment
    print("RPM or TPS missing")

