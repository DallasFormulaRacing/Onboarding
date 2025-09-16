import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cvs = pd.read_csv('can-_ecu_762.csv')

# Finding columns with null values using isNull() and any()

containNull = cvs.columns[cvs.isnull().any()]

# Array to hold constant columns

constantColumn = []

# Loop through each column in the DataFrame and append to list if constant

for col in cvs.columns:
    if cvs[col].nunique() <= 1:
        constantColumn.append(col)
    

print(containNull)
print(constantColumn)

# Using union to put everyting together and avoid duplicates
column_drop = containNull.union(constantColumn)


fixedcvs = cvs.drop(column_drop, axis=1)

print(fixedcvs)



# Graph plot for RPM and TPS using Pandas and Matplotlib

# Figure, axes = axes array(row, col, size)

'''
fig, axes = plt.subplots(3, 1, figsize=(12, 3)) #  vertical plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5)) # horizontal plots


rpmPlot = cvs.plot(x="timestamp",y="RPM", kind='line', title='RPM over Time', ax=axes[0])

tpsPlot = cvs.plot(x="timestamp",y="TPS", kind='line', title='TPS over Time', ax=axes[1] )

bothPlot = cvs.plot(x="timestamp",y=["RPM","TPS"], kind='line', title='RPM and TPS over Time', ax=axes[2] )


plt.tight_layout()
plt.show()
'''

fig = make_subplots(rows=3, cols=1, subplot_titles=("RPM over Time", "TPS over Time", "RPM and TPS over Time"))

# RPM and Plot on different rows

fig.add_trace(
    go.Scatter( x=cvs['timestamp'], y=cvs['RPM'],),
    row=1, col=1
    )
fig.add_trace(
    go.Scatter( x=cvs['timestamp'], y=cvs['TPS'],),
    row=2, col=1
    )

# Both on same row

fig.add_trace(
    go.Scatter( x=cvs['timestamp'], y=cvs['RPM'],),
    row=3, col=1
    )
fig.add_trace(
    go.Scatter( x=cvs['timestamp'], y=cvs['TPS'],),
    row=3, col=1
    )

fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_xaxes(title_text="Time", row=3, col=1)   
fig.update_yaxes(title_text="RPM", row=1, col=1)
fig.update_yaxes(title_text="TPS", row=2, col=1)
fig.update_yaxes(title_text="Value", row=3, col=1)

fig.update_layout(height=1000, title="RPM and TPS over Time")

fig.show()
