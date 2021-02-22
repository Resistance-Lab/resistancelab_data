import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')
df_2019 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2018-march2019.csv'))
df_2020 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2019-march2020.csv'))

df_2019['ytd'] = '2019-03-31'
df_2020['ytd'] = '2020-03-31'
df = pd.concat([df_2019[df_2019['Tactic'] == 'CED'], df_2020[df_2020['Tactic'] == 'CED of which']])
df = df[df['Police Force'] != "Total England and Wales"]
df = df.melt(id_vars=['Police Force', 'Tactic', 'ytd'], value_vars=['White', 'Black (or Black British)', 'Asian (or Asian British)', 'Chinese', 'Mixed', 'Other', "Don't know", 'Not reported'])

df.to_csv("taser-use-by-ethnicity.csv", index=False)
