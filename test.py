


import pandas as pd




income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]


def create_companyDF(income, expenses, years):
    df = pd.DataFrame({'Income': income,'Expenses': expenses}, index=years)
    return df
def get_profit(df,year):
    if year not in df.index:
        return None
    income = df.loc[year, 'Income']
    expenses = df.loc[year, 'Expenses']
    profit = income - expenses
    print(f"Income: {income}")
    print(f"expenses: {expenses}")
    return profit

print(get_profit(year = 2018, df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])))