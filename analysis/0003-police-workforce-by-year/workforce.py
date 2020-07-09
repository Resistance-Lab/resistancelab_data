import pandas as pd
import os

fte_root = os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_data', 'police-population', 'officer-fte')

fte_15 = pd.read_csv(os.path.join(fte_root, '2015.csv'))
fte_16 = pd.read_csv(os.path.join(fte_root, '2016.csv'))
fte_17 = pd.read_csv(os.path.join(fte_root, '2017.csv'))
fte_18 = pd.read_csv(os.path.join(fte_root, '2018.csv'))
fte_19 = pd.read_csv(os.path.join(fte_root, '2019.csv'))

fte_15.drop(["September 2014", "September 2015"], axis=1, inplace=True)
fte_15['year'] = "2015"
fte_15.columns = ["Force/Region", "FTE Count", "Year"]

fte_16.drop(["September 2015", "September 2016"], axis=1, inplace=True)
fte_16['year'] = "2016"
fte_16.columns = ["Force/Region", "FTE Count", "Year"]

fte_17.drop(["September 2016", "September 2017"], axis=1, inplace=True)
fte_17['year'] = "2017"
fte_17.columns = ["Force/Region", "FTE Count", "Year"]

fte_18.drop(["September 2017", "September 2018"], axis=1, inplace=True)
fte_18['year'] = "2018"
fte_18.columns = ["Force/Region", "FTE Count", "Year"]

fte_19.drop(["September 2018", "September 2019"], axis=1, inplace=True)
fte_19['year'] = "2019"
fte_19.columns = ["Force/Region", "FTE Count", "Year"]

output = pd.concat([fte_15, fte_16, fte_17, fte_18, fte_19])

output = output[~output["Force/Region"].str.contains("Total")]
output = output[~output["Force/Region"].isin(
    ["England and Wales", "East of England", "South West", "South East", "London", "Wales", "Yorkshire and the Humber",
     "North East", "North West", "Eastern"])]
output.rename(columns={"Force/Region": "Police force"}, inplace=True)

output.to_csv("police-workforce-fte-by-year.csv", index=False)
