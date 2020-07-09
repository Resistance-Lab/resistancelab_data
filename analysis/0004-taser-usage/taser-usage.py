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
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ced-type-force-region', 'april2018-march2019.csv'))
april_2018_march_2019['ytd'] = '2019-03-31'
april_2018_march_2019.drop(["Region"], axis=1, inplace=True)

april_2017_march_2018 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ced-type-force-region', 'april2017-march2018.csv'))
april_2017_march_2018['ytd'] = '2018-03-31'
april_2017_march_2018.drop(["Region"], axis=1, inplace=True)

january_december_2016_revised = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ced-type-force-region',
                 'january-december2016-revised.csv'))
january_december_2016_revised['ytd'] = '2016-12-31'
january_december_2016_revised.drop(["Region"], axis=1, inplace=True)

# These come from various sources around taser use
january_december2015_revised = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'taser-use', 'by-ced-type-force-region', '2015-revised.csv'))
january_december2015_revised['ytd'] = '2015-12-31'
january_december2015_revised.drop(
    ["Proportion of TASER ® X26 use - discharge", "Proportion of TASER ® X26 use - non-discharge"], axis=1,
    inplace=True)
january_december2015_revised.rename(columns={"Police Force/Region": "Police force"}, inplace=True)

# @TODO make table2-2009-2010.csv more usable

# Concat all the data
dataframes = [april_2018_march_2019, april_2017_march_2018, january_december_2016_revised, january_december2015_revised]
output = pd.concat(dataframes)
output = output[~output["Police force"].str.contains("Total")]
output = output[~output["Police force"].isin(
    ["England and Wales", "East of England", "South West", "South East", "London", "Wales", "Yorkshire and the Humber",
     "North East", "North West"])]
output.to_csv("taser-use-by-force-by-year.csv", index=False)
