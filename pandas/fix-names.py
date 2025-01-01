# https://leetcode.com/studyplan/30-days-of-pandas/
# day 7

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users["name"] = users["name"].str.capitalize()

    return users.sort_values("user_id")
