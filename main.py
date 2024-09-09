import pandas as pd
import plotly.express as px

def load_data(filename):
    return pd.read_csv(filename)

def clean_data(data):
    constant_cols = [col for col in data.columns if data[col].nunique() == 1]
    data_cleaned = data.drop(columns=constant_cols)
    return data_cleaned, constant_cols

def plot_data(data):
    if 'RPM' in data.columns and 'TPS' in data.columns:
        fig_rpm = px.scatter(data, x=data.index, y='RPM', title='RPM Over Time', labels={'index': 'Time', 'RPM': 'RPM'})
        fig_rpm.show()

        fig_tps = px.scatter(data, x=data.index, y='TPS', title='TPS Over Time', labels={'index': 'Time', 'TPS': 'TPS'})
        fig_tps.show()
    else:
        print("RPM and/or TPS columns are missing from the data.")

def main():
    filename = 'can-_ecu_762.csv' 
    data = load_data(filename)
    
    data_cleaned, removed_columns = clean_data(data)
    print(f"Removed columns: {removed_columns}")
    
    plot_data(data_cleaned)

if __name__ == "__main__":
    main()
