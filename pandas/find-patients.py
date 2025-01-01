# https://leetcode.com/studyplan/30-days-of-pandas/
# day 9

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    patients = patients[patients["conditions"].str.contains(r"(?<!\+)\bDIAB1", regex=True)]

    return patients
