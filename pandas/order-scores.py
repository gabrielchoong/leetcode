# https://leetcode.com/studyplan/30-days-of-pandas/
# day 13

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    scores = scores.sort_values(by="score")

    scores["rank"] = scores["score"].rank(method="dense", ascending=False)

    return scores[["score", "rank"]].sort_values(by="score", ascending=False)
