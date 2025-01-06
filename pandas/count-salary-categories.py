# https://leetcode.com/studyplan/30-days-of-pandas/
# day 16

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low_salary = len(accounts[accounts["income"] < 20000])

    average_salary = len(accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)])

    high_salary = len(accounts[accounts["income"] > 50000])

    return pd.DataFrame({
        "category": ["High Salary", "Average Salary", "Low Salary"],
        "accounts_count": [high_salary, average_salary, low_salary]
    })
