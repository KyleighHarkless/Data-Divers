import pandas as pd
import matplotlib.pyplot as plot

def main():
    #1. Load exported data
    income_data = pd.read_csv("income.csv")
    report(income_data)

    age_sex_data = pd.read_csv("Age and Sex.csv")
    report(age_sex_data)

    housing_data = pd.read_csv("robeson_housing.csv")
    report(housing_data)

    industry_data = pd.read_csv("industry_by_sex.csv")
    report(industry_data)  

    finance_civilian_data = pd.read_csv("financial_characteristics.csv")
    report(finance_civilian_data)

    housing_finance_data = pd.read_csv("financial_character_housing.csv")
    report(housing_finance_data)

    race_demographics = pd.read_csv("RACE.csv")
    report(race_demographics)

    transport_data = pd.read_csv("transportation.csv")
    report(transport_data)

    occupants_per_room = pd.read_csv("occupants_per_room.csv")
    report(occupants_per_room)
    
def report(df, ):
    print("\t--DataFrame Structure:--\n")
    inspect_structure(df)

    print("\n\t--Checking quality--\n")
    check_quality(df)

    print("\n\t--Validating keys--\n")
    validate_keys(df)
    print("---------------------")

def inspect_structure(df):
    df.head(5) # Display the first 5 rows of the DataFrame
    df.info() # Display summary information about the DataFrame, including data types and non-null counts

def check_quality(df):
    columns = get_columns(df)
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print(f"# of Missing Values: \n{df.isna().sum()}")
    print(f"\nSummary Stats: \n{df.describe().round(2)}")

def validate_keys(df):
    #Check for duplicate keys
    if df.duplicated().any():
        print("Duplicate keys found and removedg.")
        df = df.drop_duplicates()
    else:
        print("No duplicate keys found.")

def get_columns(df):
    columns = []
    for col in df.columns:
        if col.startswith("Label") or col.endswith("Margin of Error"):
            continue
        columns.append(col)
    
    return columns

if __name__ == "__main__":
    main()

