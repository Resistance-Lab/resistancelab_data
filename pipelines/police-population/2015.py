from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory

ods_file = download("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/494752/police-workforce-tabs-30sep15.ods")

fte_output = make_output_directory("officer-fte")
officer_fte = read_ods(ods_file, "Table_1")
officer_fte.drop([0, 1, 2, 3, 4, 62, 63, 64, 65, 66, 67, 68], inplace=True)
officer_fte.drop(["unnamed.4", "unnamed.5", "unnamed.6", "unnamed.7", "unnamed.9"], inplace=True, axis=1)
officer_fte.columns = ["Force/Region", "September 2014", "March 2015", "September 2015"]
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('Metropolitan Police', 'Metropolitan')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('London, City of', 'City of London')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace(r'\d+$', '')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.strip()
officer_fte.to_csv(os.path.join(fte_output, "2015.csv"), index=False)
