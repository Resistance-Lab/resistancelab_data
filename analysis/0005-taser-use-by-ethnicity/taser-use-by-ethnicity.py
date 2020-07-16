"""
| force | ytd | type 1 | type 2 | ... |
|------|--------------|--------|-------|------|
| Kent | 2019-03-31   | 1      |  2   |       |
...
"""

import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')


# These three years come from use-of-force data, and are all the same format
april_2018_march_2019 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2018-march2019.csv'))
april_2018_march_2019['ytd'] = '2019-03-31'
april_2018_march_2019.drop(["Region"], axis=1, inplace=True)


# Concat all the data
dataframes = [april_2018_march_2019, april_2017_march_2018, january_december_2016_revised, january_december2015_revised]
output = pd.concat(dataframes)
output = output[~output["Police force"].str.contains("Total")]
output = output[~output["Police force"].isin(
    ["England and Wales", "East of England", "South West", "South East", "London", "Wales", "Yorkshire and the Humber",
     "North East", "North West"])]
output.to_csv("taser-use-by-force-by-year.csv", index=False)
