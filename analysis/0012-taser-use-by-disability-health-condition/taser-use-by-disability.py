import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')
df_2019 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-disability-force', 'april2018-march2019.csv'))
df_2019['ytd'] = '2019-03-31'
df_2020 = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-health-condition-force', 'april2019-march2020.csv'))
df_2020['ytd'] = '2020-03-31'

df = pd.concat([df_2019, df_2020])
df = df.loc[df['Tactic'] == 'CED']
df = df[df['Police Force'] != "Total England and Wales"]
df = df.rename(columns={'Physical and mental': 'Both'})
df = df.rename(columns={'Number of times tactic reported': 'Total'})
melted = df.melt(id_vars=['Police Force', 'Tactic', 'ytd'], value_vars=['Mental', 'Physical', 'Both', 'None', 'Not reported', 'Total'])
melted
df.to_csv("taser-use-by-disability-health-condition.csv", index=False)
