# https://leetcode.com/studyplan/30-days-of-pandas/
# day 10 if you're f2p
# day 11 if you're p2w
# jk

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    if N > len(employee["salary"].unique()):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    if N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    # nlargest(N) gives the top N+1 values, so .iloc[-1] grabs the Nth largest by picking the last value in the list.

    salary = employee["salary"].drop_duplicates().nlargest(N).iloc[-1]

    string = f"getNthHighestSalary({N})"

    return pd.DataFrame({string: [salary]})
