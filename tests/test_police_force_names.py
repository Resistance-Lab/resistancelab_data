from unittest import TestCase
import pandas as pd
import os

FORCES = ["Cleveland", "Durham", "Northumbria", "Cheshire", "Cumbria", "Greater Manchester",
          "Lancashire", "Merseyside", "Humberside", "North Yorkshire",
          "South Yorkshire", "West Yorkshire", "Derbyshire", "Leicestershire", "Lincolnshire",
          "Northamptonshire", "Nottinghamshire", "Staffordshire", "Warwickshire", "West Mercia",
          "West Midlands", "Bedfordshire", "Cambridgeshire", "Essex", "Hertfordshire",
          "Norfolk", "Suffolk", "City of London", "Metropolitan", "Hampshire",
          "Kent", "Surrey", "Sussex", "Thames Valley", "Avon & Somerset", "Devon & Cornwall",
          "Dorset", "Gloucestershire", "Wiltshire", "Dyfed-Powys", "Gwent", "North Wales", "South Wales"]
FORCES.sort()
cwd = os.path.dirname(__file__)


def forces_from_csv(csv_path, heading):
    df = pd.read_csv(csv_path)
    df_forces = df[heading].to_list()
    df_forces.sort()
    return df_forces


def dedupe(my_list):
    output = list(set(my_list))
    output.sort()
    return output


class PoliceForceNames(TestCase):
    def test_taser_use_pre_2011_table1(self):
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'taser-use', 'pre-2011', 'table1-2004-2010-total.csv')
        csv_forces = forces_from_csv(csv_path, 'Force')
        self.assertEqual(FORCES, csv_forces)

    def test_taser_use_pre_2011_table2(self):
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'taser-use', 'pre-2011', 'table2-2009-2010.csv')
        csv_forces = forces_from_csv(csv_path, 'Force')
        self.assertEqual(FORCES, csv_forces)

    def test_taser_use_by_ced_type_force_region_2015_revised(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'taser-use', 'by-ced-type-force-region', '2015-revised.csv')
        csv_forces = forces_from_csv(csv_path, 'Police Force/Region')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_taser_use_by_ced_type_force_region_2016(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'taser-use', 'by-ced-type-force-region', '2016.csv')
        csv_forces = forces_from_csv(csv_path, 'Police Force/Region')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_by_age_force(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-age-force', 'april2018-march2019.csv')
        csv_forces = dedupe(forces_from_csv(csv_path, 'Police Force'))
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_by_disability_force(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-disability-force', 'april2018-march2019.csv')
        csv_forces = dedupe(forces_from_csv(csv_path, 'Police Force'))
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_by_ethnicity_force(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-ethnicity-force', 'april2018-march2019.csv')
        csv_forces = dedupe(forces_from_csv(csv_path, 'Police Force'))
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_by_ced_type_force_region_march_2018(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-ced-type-force-region', 'april2017-march2018.csv')
        csv_forces = forces_from_csv(csv_path, 'Police force')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    # This test is deliberately disabled - it fails because a number of forces haven't actually reported this data
    # def test_use_of_force_by_ced_type_force_region_march_2019(self):
    #     self.maxDiff = 2000
    #     csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-ced-type-force-region',
    #                             'april2018-march2019.csv')
    #     csv_forces = forces_from_csv(csv_path, 'Police force')
    #     # self.assertTrue(set(FORCES).issubset(set(csv_forces)))
    #     self.assertEqual(FORCES, csv_forces)

    def test_use_of_force_by_ced_type_force_region_december_2016(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-ced-type-force-region',
                                'january-december2016-revised.csv')
        csv_forces = forces_from_csv(csv_path, 'Police force')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_by_ced_type_force_region_march2017(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'by-ced-type-force-region',
                                'january-march2017.csv')
        csv_forces = forces_from_csv(csv_path, 'Police force')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_incidents_2018(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'incidents',
                                'april2017-march2018.csv')
        csv_forces = forces_from_csv(csv_path, 'Police Force')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def test_use_of_force_incidents_2019(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'use-of-force', 'incidents',
                                'april2018-march2019.csv')
        csv_forces = forces_from_csv(csv_path, 'Police Force')
        self.assertTrue(set(FORCES).issubset(set(csv_forces)))

    def police_population_fte_2019(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'police-population', 'officer-fte','2019.csv')
        csv_forces = forces_from_csv(csv_path, 'Force/Region')
        self.assertEqual(FORCES, csv_forces)

    def police_population_headcount_2019(self):
        self.maxDiff = 2000
        csv_path = os.path.join(cwd, '..', 'cleaned_data', 'police-population', 'officer-headcount','2019.csv')
        csv_forces = forces_from_csv(csv_path, 'Force/Region')
        self.assertEqual(FORCES, csv_forces)
