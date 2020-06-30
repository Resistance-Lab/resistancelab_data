from unittest import TestCase
import great_expectations as ge

context = ge.data_context.DataContext()


def run_great_expectations(path, suite_name):
    batch_kwargs = {"path": path, "datasource": "files_datasource"}
    batch = context.get_batch(batch_kwargs, suite_name)
    results = context.run_validation_operator("action_list_operator", [batch])
    return results


class Tasers2016(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "tasers-2016.warning"

    def test_2015(self):
        validation_result = run_great_expectations("output/use-of-force/by-ced-type-force-region/2015-revised.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_2016(self):
        validation_result = run_great_expectations("output/use-of-force/by-ced-type-force-region/2016.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class Tasers2018(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "tasers-2018.warning"

    def test_2018(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-ced-type-force-region/april2017-march2018.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_2019(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-ced-type-force-region/april2018-march2019.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_2016_revised(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-ced-type-force-region/january-december2016-revised.csv",
            self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_2017(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-ced-type-force-region/january-march2017.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class TasersType(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "tasers-by-type.warning"

    def test_historic(self):
        validation_result = run_great_expectations("output/use-of-force/historic-ced-usage/2011-2016.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class UseOfForceIncidents(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "police-force-incidents.warning"

    def test_2019(self):
        validation_result = run_great_expectations("output/use-of-force/incidents/april2018-march2019.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_2018(self):
        validation_result = run_great_expectations("output/use-of-force/incidents/april2017-march2018.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class UseOfForceByEthnicity(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "police-force-ethnicity.warning"

    def test_2019(self):
        validation_result = run_great_expectations("output/use-of-force/by-ethnicity-force/april2018-march2019.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class UseOfForceByDisability(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "police-force-disability.warning"

    def test_2019(self):
        validation_result = run_great_expectations("output/use-of-force/by-disability-force/april2018-march2019.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class UseOfForceByAge(TestCase):
    def setUp(self) -> None:
        self.expectation_suite_name = "police-force-age.warning"

    def test_2019(self):
        validation_result = run_great_expectations("output/use-of-force/by-age-force/april2018-march2019.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class PolicePopulation(TestCase):
    def setUp(self):
        self.expectation_suite_name = "police-population.warning"

    def test_2020(self):
        validation_result = run_great_expectations("output/police-population/year=2020/police-population.csv",
                                                   self.expectation_suite_name)
        self.assertTrue(validation_result['success'])


class PoliceNumbers(TestCase):
    def test_historic(self):
        validation_result = run_great_expectations("output/police-population/historic/police-numbers.csv",
                                                   "police-numbers.warning")
        self.assertTrue(validation_result['success'])


class MeltedUseOfCorce(TestCase):
    def setUp(self):
        self.expectation_suite_name = "melted.warning"

    def test_disability(self):
        validation_result = run_great_expectations("output/use-of-force/by-disability-force/april2018-march2019-melted.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_ethnicity(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-ethnicity-force/april2018-march2019-melted.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])

    def test_age(self):
        validation_result = run_great_expectations(
            "output/use-of-force/by-age-force/april2018-march2019-melted.csv", self.expectation_suite_name)
        self.assertTrue(validation_result['success'])
