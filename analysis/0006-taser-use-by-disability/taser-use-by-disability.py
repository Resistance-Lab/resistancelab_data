import pandas as pd
import os

repo_root = os.path.join("/Users/kim/src/resistancelab_data")
df = pd.read_csv(
    os.path.join(repo_root, 'cleaned_data', 'use-of-force', 'by-disability-force', 'april2018-march2019.csv'))
df['ytd'] = '2019-03-31'
df = df.loc[df['Tactic'] == 'CED']
df = df[df['Police Force'] != "Total England and Wales"]
df = df.rename(columns={'Physical and mental': 'Both'})
df = df.rename(columns={'Number of times tactic reported': 'Total'})
melted = df.melt(id_vars=['Police Force', 'Tactic'], value_vars=['Mental', 'Physical', 'Both', 'None', 'Not reported', 'Total'])
melted
df.to_csv("analysis/0005-taser-use-by-disability/taser-use-by-disability.csv", index=False)
