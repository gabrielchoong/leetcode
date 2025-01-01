# https://leetcode.com/studyplan/30-days-of-pandas/
# day 5

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    tweets = tweets[tweets["content"].str.len() > 15]

    return tweets[["tweet_id"]]
