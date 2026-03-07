import pandas as pd
import matplotlib.pyplot as plot
import csv

def main():
    #1. Load exported data
    housing_data = pd.read_csv("Housing_Unit_Data.csv")
    report(housing_data)

    income_data = pd.read_csv("income.csv")
    report(income_data)

    agesex_data = pd.read_csv("Age and Sex.csv")
    report(agesex_data)
    
def report(df):
    #2. Inspect structure
    print("--DataFrame Structure:--")
    
    df.head(3) # Display the first 3 rows of the DataFrame
    df.info() # Display summary information about the DataFrame, including data types and non-null counts
    
    #3. Check data quality
    print("\n--Checking for missing values--\n")
    print(f"Check for missing Values: {df.isna().sum()}")
    print(f"Summary Stats: \n{df.describe()}")

    #4. Validate keys
    print("---------------------")

if __name__ == "__main__":
    main()
