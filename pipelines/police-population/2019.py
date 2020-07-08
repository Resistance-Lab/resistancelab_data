from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory

ods_file = download("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/861796/police-workforce-sep19-tables.ods")

headcount_output = make_output_directory("officer-headcount")
officer_headcount = read_ods(ods_file, "Table_7")
officer_headcount.drop([0, 1, 2, 3, 4, 61, 62, 63, 64, 65, 58], inplace=True)
officer_headcount.columns = ["Force/Region", "March 2019", "September 2019", "increase", "pct increase"]
officer_headcount['Force/Region'] = officer_headcount['Force/Region'].str.replace('Metropolitan Police', 'Metropolitan')
officer_headcount['Force/Region'] = officer_headcount['Force/Region'].str.replace('London, City of', 'City of London')
officer_headcount['Force/Region'] = officer_headcount['Force/Region'].str.strip()
officer_headcount.to_csv(os.path.join(headcount_output, "2019.csv"), index=False)

fte_output = make_output_directory("officer-fte")
officer_fte = read_ods(ods_file, "Table_1")
officer_fte.drop([0, 1, 2, 3, 4, 61, 62, 63, 64, 65, 66], inplace=True)
officer_fte.drop(["unnamed.4", "unnamed.5", "unnamed.6", "unnamed.7"], inplace=True, axis=1)
officer_fte.columns = ["Force/Region", "September 2018", "March 2019", "September 2019"]
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('Metropolitan Police', 'Metropolitan')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.replace('London, City of', 'City of London')
officer_fte['Force/Region'] = officer_fte['Force/Region'].str.strip()
officer_fte.to_csv(os.path.join(fte_output, "2019.csv"), index=False)
