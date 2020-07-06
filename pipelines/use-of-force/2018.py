import pandas as pd
from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory


def save_sheet(sheet, title, filename):
    directory = make_output_directory('by-ced-type-force-region')
    df = read_ods(output_file, sheet)

    # Drop the empty rows
    df.drop([0, 1, 57, 58, 59, 60, 61], inplace=True)

    # Build a new dataframe with correct column names
    cleansed = pd.DataFrame(
        {"Region": df[title],
         "Police force": df['unnamed.1'].str.rstrip(),
         "Total": df['unnamed.2'],
         "Total non-discharge": df['unnamed.3'],
         "Drawn": df['unnamed.4'],
         "Aimed": df['unnamed.5'],
         "Red-dot": df['unnamed.6'],
         "Arced": df['unnamed.7'],
         "Total discharge": df['unnamed.8'],
         "Drive stun": df['unnamed.9'],
         "Fired": df['unnamed.10'],
         "Angled drive stun": df['unnamed.11'],
         "Not stated": df['unnamed.12']})[1:]

    # Write to file
    cleansed.to_csv(os.path.join(directory, filename), index=False)


# Because of course the revised figures are in a different format to the other figures
def save_revised_sheet(sheet, title, filename):
    directory = make_output_directory('by-ced-type-force-region')

    df = read_ods(output_file, sheet)

    # Drop the empty rows
    df.drop([0, 1, 57, 58, 59, 60, 61, 62], inplace=True)

    # Build a new dataframe with correct column names
    cleansed = pd.DataFrame(
        {
            "Region": df[title],
            "Police force": df['unnamed.1'],
            "Total": df['unnamed.2'],
            "Total non-discharge": df['unnamed.4'],
            "Drawn": df['unnamed.6'],
            "Aimed": df['unnamed.8'],
            "Red-dot": df['unnamed.10'],
            "Arced": df['unnamed.12'],
            "Total discharge": df['unnamed.14'],
            "Drive stun": df['unnamed.16'],
            "Fired": df['unnamed.18'],
            "Angled drive stun": df['unnamed.20'],
            "Not stated": df['unnamed.22']
        }
    )[1:]
    cleansed.to_csv(os.path.join(directory, filename), index=False)


def save_incidents():
    directory = make_output_directory("incidents")
    df = read_ods(output_file, "Table_12")
    df.drop([0, 1, 2, 57, 58, 59], inplace=True)
    cleansed = pd.DataFrame(
        {
            "Region": df['Table 12. Incidents by police force'],
            "Police Force": df['unnamed.1'],
            "Total": df['unnamed.2']
        }
    )
    cleansed.to_csv(os.path.join(directory, "april2017-march2018.csv"), index=False)


if __name__ == '__main__':

    # Download the file into the raw directory
    ods_file_2018 = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/764895/police-use-of-force-apr2017-mar2018-hosb3018-tables.ods'
    output_file = download(ods_file_2018)

    # Save the relevant sheets
    save_sheet('Table_13', 'Table 13. Use of CED by type and police force: 1 April 2017 to 31 March 2018',
               'april2017-march2018.csv')
    save_sheet('Table_14', 'Table 14. Use of CED by type and police force: January to March 2017',
               'january-march2017.csv')
    save_revised_sheet('Table_15', 'Table 15. Use of CED by type and police force: January to December 2016 revisions',
                       'january-december2016-revised.csv')
    save_incidents()
