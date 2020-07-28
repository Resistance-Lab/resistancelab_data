import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')

# df_2009_2010 = pd.read_csv(os.path.join(repo_root, "cleaned_data", "taser-use", "pre-2011", "table2-2009-2010.csv"))
# @todo the source data doesn't quite add up, so we are using the totals from table 2 of https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/115676/taser-figures-march-2010.pdf
df_2009_2010_rebuilt = pd.DataFrame({
    "Not stated": [0],
    "Total discharge": [896],
    "Total non-discharge": [2677],
    "Total": [3573],
    "Year": ["2009-10"]
})
# print(df_2009_2010_rebuilt)

df_2011_2016 = pd.read_csv(os.path.join(repo_root, "cleaned_data", "taser-use", "historic-ced-usage", "2011-2016.csv"))
df_2011_2016 = df_2011_2016.transpose()  # @todo why can't transpose just set the column names correctly?
df_2011_2016 = df_2011_2016[1:]
df_2011_2016.columns = ["Drawn", "Aimed", "Arced", "Red-dot", "Total non-discharge", "Drive stun", "Angled drive stun", "Fired", "Total discharge", "Not stated", "Total"]
df_2011_2016.drop(["Numeric change between 2015 to 2016", "% change between 2015 to 2016"], inplace=True)
df_2011_2016['Year'] = df_2011_2016.index
# print(df_2011_2016)

df_2017_2018 = pd.read_csv(os.path.join(repo_root, "cleaned_data", "use-of-force", "by-ced-type-force-region", "april2017-march2018.csv"))
df_2017_2018 = df_2017_2018[df_2017_2018['Police force'] == '*Total England and Wales']
df_2017_2018.drop(["Police force", "Region"], inplace=True, axis=1)
df_2017_2018['Year'] = '2017-18'
# print(df_2017_2018)

df_2018_2019 = pd.read_csv(os.path.join(repo_root, "cleaned_data", "use-of-force", "by-ced-type-force-region", "april2018-march2019.csv"))
df_2018_2019 = df_2018_2019[df_2018_2019['Police force'] == '*Total England and Wales']
df_2018_2019.drop(["Police force", "Region"], inplace=True, axis=1)
df_2018_2019['Year'] = '2018/19'
# print(df_2018_2019)

total = pd.concat([df_2009_2010_rebuilt, df_2011_2016, df_2017_2018, df_2018_2019])
print(total)

total.to_csv("total.csv", index=False)
