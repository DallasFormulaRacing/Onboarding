import pandas as pd
import plotly.express as pe

df = pd.read_csv("can_data.csv")

print(df.columns)


for col in df.columns:
    if "Analog Input" in col and df[col].nunique() == 1:
        df.drop(columns = col, inplace = True)

rpm = pe.line(df, x = "timestamp", y = "RPM", title = "RPM Over Time")
rpm.show()

tps = pe.line(df, x = "timestamp", y = "TPS", title = "TPS Over Time")
tps.show()
