from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory

ods_file = download("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/675788/police-workforce-tables-jan17.ods")

fte_output = make_output_directory("officer-fte")
officer_fte = read_ods(ods_file, "Table_1")
officer_fte.drop([0, 1, 2, 3, 4, 5, 62, 63, 64, 65, 66, 67], inplace=True)
print(officer_fte)
officer_fte.drop(["unnamed.4", "unnamed.5", "unnamed.6", "unnamed.7"], inplace=True, axis=1)
officer_fte.columns = ["Force/Region", "September 2016", "March 2017", "September 2017"]
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('Metropolitan Police', 'Metropolitan')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('London, City of', 'City of London')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.strip()
officer_fte.to_csv(os.path.join(fte_output, "2017.csv"), index=False)
