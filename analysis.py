import pandas as pd
import matplotlib.pyplot as plot
import csv

def main():
    #1. Load exported data
    housing_data = pd.read_csv("Housing_Unit_Data.csv")
    report(housing_data)

    income_data = pd.read_csv("Income_Data.csv")
    report(income_data)

    agesex_data = pd.read_csv("Age and Sex.csv")
    report(agesex_data)
    
def report(df):
    #2. Inspect structure
    rows = df.shape[0]
    columns = df.shape[1]
    print(f"Rows: {rows}, Columns: {columns}")
    df.head() # Display the first 5 rows of the DataFrame
    df.info() # Display summary information about the DataFrame, including data types and non-null counts
    
    #3. Check data quality
    print("---------------------")
    print(df.isna().sum())
    print(df.describe())
    #4. Validate keys

if __name__ == "__main__":
    main()
