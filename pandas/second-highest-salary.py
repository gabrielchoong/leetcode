# https://github.com/gabrielchoong/leetcode/new/main/pandas
# day 11


# This is just nth-highest-salary but hardcoded nlargest(2)

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    text = "SecondHighestSalary"

    salary = employee["salary"].drop_duplicates().nlargest(2).iloc[-1]

    return pd.DataFrame({text: [salary]})
