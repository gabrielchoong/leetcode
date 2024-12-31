# Question: https://leetcode.com/studyplan/30-days-of-pandas/
# day 4

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    views = views[views['author_id'] == views['viewer_id']]

    id = pd.unique(views["author_id"])

    return pd.DataFrame({"id": id}).sort_values("id")
