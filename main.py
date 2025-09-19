import pandas as pd
import numpy as np
import plotly.express as px
print("hello world my changes")

mycsv = pd.read_csv("can_data.csv")

for column in mycsv:
    validColumn = False
    # mycsv[column].head()
    if "Analog Input" in column:
        initialValue = None
        for row in enumerate(mycsv[column]):
            if pd.isna(row[1]):
                continue
            elif initialValue is None:
                initialValue = row[1]
            if row[1] != initialValue:
                print("\n", row[1], " at index ", row[0], " is not equal to ", initialValue, "!\n")
                validColumn = True
                break
        if validColumn == False:
            mycsv.drop(column, axis=1, inplace=True)

mycsv.to_csv('output.csv', index=False)

fig1 = px.scatter(mycsv, x="timestamp", y="RPM")
fig1.update_layout(title = dict(text = "Rotations per Minute over Time"), xaxis=dict(title=dict(text = "Timestamp")), yaxis=dict(title=dict(text= "Rotations per Minute")))
fig2 = px.scatter(mycsv, x="timestamp", y="TPS", labels=[])
fig2.update_layout(title = dict(text = "TPS over Time"), xaxis=dict(title=dict(text = "Timestamp")), yaxis=dict(title=dict(text= "TPS")))

fig1.show()
fig2.show()