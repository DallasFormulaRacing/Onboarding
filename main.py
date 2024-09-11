#import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

#retrieving the csv file and reading the file
file_path = r'C:\Users\Downloads\can-_ecu_762.csv'
data = pd.read_csv(file_path)

#storing the particular columns as variables
x = data['timestamp']
y1 = data['RPM']
y2 = data['TPS']
y3 = y1 * y2

plt.style.use('dark_background')
# Create subplots
plt.figure(figsize=(10, 8))

# First plot (for RPM)
plt.subplot(3, 1, 1)
plt.plot(x, y1)
plt.title('RPM vs Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('RPM')

# Second plot (for TPS)
plt.subplot(3, 1, 2)
plt.plot(x, y2, color ='r')
plt.title('TPS vs Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('TPS')

# Third plot (for Power)
plt.subplot(3, 1, 3)
plt.plot(x, y3, color ='b')
plt.title('Power vs Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('Power')

#plot the graphs
plt.tight_layout()
plt.show()

