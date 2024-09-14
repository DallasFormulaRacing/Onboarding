import pandas as pd

df = pd.read_csv('can-_ecu_762.csv')
analog_columns = df.iloc[:, 1:9]
df.drop(analog_columns.columns[analog_columns.nunique() <= 1], axis=1, inplace=True)
df.to_csv('cleaned_data.csv')

pd.options.plotting.backend = 'plotly'
rpm = df.loc[:, ['timestamp', 'RPM']]
tps = df.loc[:, ['timestamp', 'TPS']]

rpm_graph = rpm.plot(title='RPM vs. Time', labels=dict(timestamp='Time', index='RPM'), x='timestamp')
tps_graph = tps.plot(title='TPS vs. Time', labels=dict(timestamp='Time', index='TPS'), x='timestamp')

rpm_graph.show()
tps_graph.show()