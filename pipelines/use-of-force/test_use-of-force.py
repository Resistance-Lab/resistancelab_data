from unittest import TestCase
import great_expectations as ge

context = ge.data_context.DataContext()


def run_great_expectations(path, suite_name):
    batch_kwargs = {"path": path, "datasource": "files_datasource"}
    batch = context.get_batch(batch_kwargs, suite_name)
    results = context.run_validation_operator("action_list_operator", [batch])
    return results


class UseOfForce(TestCase):
    def test_by_age_2019(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-age-force/april2018-march2019.csv", "use-of-force.by-age-force")
        self.assertTrue(validation_result['success'])

    def test_by_disability_2019(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-disability-force/april2018-march2019.csv", "use-of-force.by-disability-force")
        self.assertTrue(validation_result['success'])

    def test_by_ethnicity_2019(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-ethnicity-force/april2018-march2019.csv", "use-of-force.by-ethnicity-force")
        self.assertTrue(validation_result['success'])

    def test_by_age_2020(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-age-force/april2019-march2020.csv", "use-of-force.by-age-force")
        self.assertTrue(validation_result['success'])

    def test_by_health_condition_2020(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-health-condition-force/april2019-march2020.csv", "use-of-force.by-health-condition-force")
        self.assertTrue(validation_result['success'])

    def test_by_ethnicity_2020(self):
        validation_result = run_great_expectations("../../cleaned_data/use-of-force/by-ethnicity-force/april2019-march2020.csv", "use-of-force.by-ethnicity-force-2020")
        self.assertTrue(validation_result['success'])
