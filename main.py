import pandas as pd
import plotly.express as px

df = pd.read_csv('can-_ecu_762.csv')
#make list to store dropped cols
cols_to_drop = []
for i in range(len(df.columns)):
    #get first value of each col and store in temp
    temp = df.iloc[0, i]
    #Check if each value in col = first value
    allSame = True
    for value in df.iloc[:, i]:
        if value != temp:
            allSame = False
            break
    #If all values are =, add to columns to drop list
    if allSame:
        cols_to_drop.append(df.columns[i])
#Drop columns where are values are same
df = df.drop(columns = cols_to_drop)

# TODO: you don't want to overwrite the OG, it's bad practice 
df.to_csv('can-_ecu_762.csv', index = False) 
print(f"Columns dropped: {cols_to_drop}")
print(df.head())

# solid use of df.index but maybe just hardcode the timestamp field? index can change 
figRPM = px.line(df, x = df.index, y = 'RPM', title = 'RPM Over Time')
figRPM.show()

figTPS = px.line(df, x = df.index, y = 'TPS', title = 'TPS Over Time')
figTPS.show()

figScatter = px.scatter(df, x = 'RPM', y = 'TPS', title = 'TPS Vs. RPM')
figScatter.show()