from unittest import TestCase
import great_expectations as ge

context = ge.data_context.DataContext()


def run_great_expectations(path, suite_name):
    batch_kwargs = {"path": path, "datasource": "files_datasource"}
    batch = context.get_batch(batch_kwargs, suite_name)
    results = context.run_validation_operator("action_list_operator", [batch])
    return results


class PolicePopulation(TestCase):
    def test_fte(self):
        validation_result = run_great_expectations("../../cleaned_data/police-population/officer-fte/2019.csv", "police-population.officer-fte")
        self.assertTrue(validation_result['success'])

    def test_headcount(self):
        validation_result = run_great_expectations("../../cleaned_data/police-population/officer-headcount/2019.csv", "police-population.officer-headcount")
        self.assertTrue(validation_result['success'])
