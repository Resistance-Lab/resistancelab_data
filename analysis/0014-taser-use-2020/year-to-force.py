#              ,date1,date2,date2
# police_force1,value1,value2,value3
# police_force2,value1,value2,value3

import pandas as pd

# These three years come from use-of-force data, and are all the same format

taser_use = pd.read_csv('taser-use-by-force-by-year.csv')

taser_use.drop(columns=['Drawn', 'Aimed', 'Red-dot', 'Arced', 'Drive stun', 'Angled drive stun', 'Fired', 'Not stated', 'Total non-discharge', 'Total discharge'], inplace=True)

pivoted = taser_use.pivot_table(index='Police force', columns='ytd', values='Total')
pivoted.to_csv("year-to-force.csv")
