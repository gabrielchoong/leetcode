# https://leetcode.com/studyplan/30-days-of-pandas/
# day 18

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date':'first_login'})
