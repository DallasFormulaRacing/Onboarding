import numpy as np
import pandas as pd
import plotly.express as px


data = pd.read_csv('can-_ecu_762.csv')

M, N = data.shape

columns_to_delete = []
for col in range(1, 9): #1 to column 8 are analog inputs
    non_null_mask = data.iloc[1:, col].notnull() #mask in order to take out the nan values
    if np.all(data.iloc[1:, col][non_null_mask].astype('float') == data.iloc[(M//2), col].astype('float')):
        columns_to_delete.append(col)

data.drop(data.columns[columns_to_delete], axis=1, inplace=True) # gets rid of the columns that have the same data

#data has now gotten rid of 
print('altered data: \n', data)


#graph RPM VS TPS
fig = px.scatter(data, x="RPM", y="TPS")
fig.update_layout(title='RPM vs TPS')
fig.show()


