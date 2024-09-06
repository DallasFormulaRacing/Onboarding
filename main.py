import pandas as pd  # import pandas
import plotly.express as px  # import plotly

df = pd.read_csv('can-_ecu_762.csv')  # load csv as dataframe
columnList = df.columns.values.tolist()  # make a list of every column

# To find and remove each column which static values
for column in columnList:  # iterate through columns
    i = 0  # index
    while df.isna().at[i, column]:  # find where the values begin in case of null intro
        i += 1

    # how long can we increase the index before the next value doesn't equal the current value
    while i < len(df) - 1 and df.at[i, column] == df.at[i + 1, column]:
        i += 1
    # any indices as long the column have never changed values, so we remove the column
    if i > len(df) - 2:
        print(f'{column} is STATIC')
        df.drop(column, axis=1, inplace=True)
    # My last exposure to Python and dataframes was like 4 years ago
    # so this probably sucks more than I realize, please forgive me haha

print('\nNew List:')  # demonstrate changed list
for column in df.columns.values.tolist():
    print(f'\t{column}')

# plot data
px.line(df, x='timestamp', y='TPS').show()
px.line(df, x='timestamp', y='RPM').show()
