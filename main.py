# Read CSV via pandas
# Change both RPM and TPS to Arrays
# Make a for loop
# Run RPM and TPS through that loop, removing null values
# Take those values and graph it via Plotly

import pandas as pd

rpm = pd.read_csv("can_data.csv", usecols=["RPM"]);
tps = pd.read_csv("can_data.csv", usecols=["TPS"]);

rpm = rpm.dropna();
tps = tps.dropna();

print(rpm)
print(tps)