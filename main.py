
# FILEPATH: Untitled-1
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import cm 



data = pd.read_csv('CSV/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
print(data.head())
# print rows where label is DDos
print(data.loc[data[' Label'] == 'DDoS'])


# Get the feature names
features_names = data.columns.tolist()

print(features_names)

X_data = data[features_names]
y_data = data[' label']

target_names = ['BENIGN', 'DDoS','PortScan', 'Bot', 'Infiltration', 'Web Attack', 'Brute Force', 'SQL Injection']
scaler = MinMaxScaler()
first_row_without_last_column = data.iloc[0, :-1]
print(first_row_without_last_column)
