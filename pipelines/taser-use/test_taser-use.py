from unittest import TestCase
import great_expectations as ge

context = ge.data_context.DataContext()


def run_great_expectations(path, suite_name):
    batch_kwargs = {"path": path, "datasource": "files_datasource"}
    batch = context.get_batch(batch_kwargs, suite_name)
    results = context.run_validation_operator("action_list_operator", [batch])
    return results


class TaserUse(TestCase):
    def test_historic(self):
        validation_result = run_great_expectations("../../cleaned_data/taser-use/historic-ced-usage/2011-2016.csv", "taser-use.historic-ced-usage")
        self.assertTrue(validation_result['success'])

    def test_by_ced_type_force_region(self):
        validation_result = run_great_expectations("../../cleaned_data/taser-use/by-ced-type-force-region/2015-revised.csv",
                                                   "taser-use.by-ced-type-force-region")
        self.assertTrue(validation_result['success'])

        validation_result = run_great_expectations("../../cleaned_data/taser-use/by-ced-type-force-region/2016.csv",
                                                   "taser-use.by-ced-type-force-region")
        self.assertTrue(validation_result['success'])
