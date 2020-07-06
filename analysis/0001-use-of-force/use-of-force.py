import os
from pathlib import Path
import pandas as pd

cwd = os.path.dirname(__file__)


def by_disability():
    by_type("disability")


def by_ethnicity():
    by_type("ethnicity")


def by_age():
    by_type("age")


def by_type(breakdown_type):
    Path(f"by-{breakdown_type}").mkdir(exist_ok=True)
    df = pd.read_csv(
        os.path.join(cwd, '..', '..', 'cleaned_data', 'use-of-force', f"by-{breakdown_type}-force", 'april2018-march2019.csv'))
    mapping = pd.read_csv('force-mappings.csv').set_index("Tactic - Input")
    cleansed = df.join(mapping, on=["Tactic"]).drop("Type of force - Input", axis=1)
    cleansed.to_csv(os.path.join(f"by-{breakdown_type}", "april2018-march2019.csv"), index=False)

    rebuilt = cleansed.drop(columns=["Number of times tactic reported", "Type of force"])
    melted = rebuilt.melt(
        ["Tactic", "Police Force", "Force type - Output", "Tactic - Output"], var_name=breakdown_type,
        value_name="count")
    melted.to_csv(os.path.join(f"by-{breakdown_type}", "april2018-march2019-melted.csv"), index=False)


if __name__ == '__main__':
    by_disability()
    by_ethnicity()
    by_age()
