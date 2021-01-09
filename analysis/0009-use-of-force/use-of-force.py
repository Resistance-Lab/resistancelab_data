import os
from pathlib import Path
import pandas as pd

cwd = os.path.dirname(__file__)


def by_disability():
    by_type("disability", "april2018-march2019")
    by_type("health-condition", "april2019-march2020")


def by_ethnicity():
    by_type("ethnicity", "april2018-march2019")
    by_type("ethnicity", "april2019-march2020")


def by_age():
    by_type("age", "april2018-march2019")
    by_type("age", "april2019-march2020")


def by_type(breakdown_type, year):
    Path(f"by-{breakdown_type}").mkdir(exist_ok=True)
    df = pd.read_csv(
        os.path.join(cwd, '..', '..', 'cleaned_data', 'use-of-force', f'by-{breakdown_type}-force',
                     f'{year}.csv'))
    mapping = pd.read_csv('force-mappings.csv').set_index("Tactic - Input")
    cleansed = df.join(mapping, on=["Tactic"]).drop("Type of force - Input", axis=1)
    cleansed = cleansed[~cleansed["Police Force"].isin(["Total England and Wales"])]
    cleansed.to_csv(os.path.join(f"by-{breakdown_type}", f"{year}.csv"), index=False)

    rebuilt = cleansed.drop(columns=["Number of times tactic reported", "Type of force"])
    melted = rebuilt.melt(
        ["Tactic", "Police Force", "Force type - Output", "Tactic - Output"], var_name=breakdown_type,
        value_name="count")
    melted.to_csv(os.path.join(f"by-{breakdown_type}", f"{year}-melted.csv"), index=False)


if __name__ == '__main__':
    by_disability()
    by_ethnicity()
    by_age()
