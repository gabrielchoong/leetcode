# https://leetcode.com/studyplan/30-days-of-pandas/
# day 12

# set theory: https://stackoverflow.com/questions/53645882/pandas-merging-101

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    department["departmentId"] = department["id"]

    department["Department"] = department["name"]

    employee["Employee"] = employee["name"]

    employee["Salary"] = employee["salary"]

    merge = pd.merge(
        department[["Department", "departmentId"]],
        employee[["Employee", "Salary", "departmentId"]], 
        on="departmentId",
        how="outer",
    )

    merge["Highest_salary"] = merge.groupby("departmentId")[["Salary"]].transform(max)

    return merge[merge["Salary"] == merge["Highest_salary"]][["Department", "Employee", "Salary"]]
