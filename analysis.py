import pandas as pd
import matplotlib.pyplot as plot
import csv

def main():
    #1. Load exported data
    data_file = pd.read_csv("Housing_Unit_Data.csv")
    #2. Inspect structure
    data_file.info()
    data_file.head()
    #3. Check data quality
    print(data_file.isna().sum())
    print(data_file.describe())
    #4. Validate keys

if __name__ == "__main__":
    main()
