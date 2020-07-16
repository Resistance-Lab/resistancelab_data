"""
| force | ytd | type 1 | type 2 | ... |
|------|--------------|--------|-------|------|
| Kent | 2019-03-31   | 1      |  2   |       |
...
"""

import pandas as pd
import os

repo_root = '/Users/kim/src/resistancelab_data'
df = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2018-march2019.csv'))
df['ytd'] = '2019-03-31'
df = df.loc[df['Tactic'] == 'CED']
df = df[df['Police Force'] != "Total England and Wales"]
df = df.melt(id_vars=['Police Force', 'Tactic'], value_vars=['White', 'Black (or Black British)', 'Asian (or Asian British)', 'Chinese', 'Mixed', 'Other', "Don't know", 'Not reported'])

df.to_csv("analysis/0005-taser-use-by-ethnicity/taser-use-by-ethnicity.csv", index=False)
