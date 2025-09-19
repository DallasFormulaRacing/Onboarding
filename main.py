import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt 
df = pd.read_csv("can_data.csv")

for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df.drop(columns=[col], inplace=True)

plt.figure(figsize=(10,6)) 
plt.plot(df['timestamp'], df['RPM'], label='RPM', color='blue')
plt.plot(df['timestamp'], df['TPS'], label='TPS', color='red')

plt.title('RPM and TPS over Time')
plt.xlabel('timestamp')
plt.ylabel('RPM and TPS values')
plt.legend()
plt.grid(True)
plt.show()
