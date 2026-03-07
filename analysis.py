import pandas as panda
import matplotlib.pyplot as plot
import csv

def main():
    #1. Load exported data
    data_file = panda.read_csv("Housing_Unit_Data.csv", parse_dates=["Date"])
    #2. Inspect structure
    print(data_file.info())
    #3. Check data quality
    #4. Validate keys
if __name__ == "__main__":
    main()
