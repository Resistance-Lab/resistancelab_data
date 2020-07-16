import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')
df = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2018-march2019.csv'))
df['ytd'] = '2019-03-31'
df = df.loc[df['Tactic'] == 'CED']
df = df[df['Police Force'] != "Total England and Wales"]
df = df.melt(id_vars=['Police Force', 'Tactic'], value_vars=['White', 'Black (or Black British)', 'Asian (or Asian British)', 'Chinese', 'Mixed', 'Other', "Don't know", 'Not reported'])

df.to_csv("taser-use-by-ethnicity.csv", index=False)
