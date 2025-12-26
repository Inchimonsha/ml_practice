import pandas_cl as pd
import pyarrow as par

def ts1():
    melbourne_file_path = "train.csv"
    melbourne_data = pd.read_csv(melbourne_file_path)
    #print(melbourne_data.describe())
    print(melbourne_data.columns)

if __name__ == '__main__':
    ts1()