# https://leetcode.com/studyplan/30-days-of-pandas/
# day 8

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    regex = r'^[a-zA-Z][\w.-]*@leetcode\.com$'
    
    users = users[users["mail"].str.contains(regex)]

    return users
