import pandas as pd
from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory

# Download the file into the raw directory
output_file = download(
    'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/607748/police-use-of-conducted-energy-devices-2016.ods')


def save_yearly_sheet():
    directory = make_output_directory("historic-ced-usage")
    # Load Table_1
    sheet_idx = 2
    df = read_ods(output_file, sheet_idx)

    # Drop the empty rows
    df.drop([0, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], inplace=True)
    # Build a clean dataframe from the columns which are useful
    # No, you can't just choose your columns in `read_ods`, that doesn't work for messy data
    cleansed = pd.DataFrame(
        {"Action": df['Table 1: Police use of TASER ® X26 by type, England and Wales, 2011 to 2016'],
         "2011": df['unnamed.1'],
         "2012": df['unnamed.3'],
         "2013": df['unnamed.5'],
         "2014": df['unnamed.7'],
         "2015": df['unnamed.9'],
         "2016": df['unnamed.11'],
         "Numeric change between 2015 to 2016": df['unnamed.13'],
         "% change between 2015 to 2016": df['unnamed.14']})[1:]

    # Write out the resulting dataframe to a csv
    cleansed.to_csv(os.path.join(directory, '2011-2016.csv'), index=False)


def save_annual_by_force_sheet(sheet, title, filename):
    directory = make_output_directory("by-ced-type-force-region")
    df = read_ods(output_file, sheet)

    # Drop the empty rows
    df.drop([56, 57, 58, 59, 60, 61], inplace=True)
    # Build a clean dataframe from the columns which are useful
    # No, you can't just choose your columns in `read_ods`, that doesn't work for messy data
    cleansed = pd.DataFrame(
        {"Police Force/Region": df[title].str.rstrip(),
         "Drawn": df['unnamed.1'],
         "Aimed": df['unnamed.3'],
         "Arced": df['unnamed.5'],
         "Red-dot": df['unnamed.7'],
         "Total non-discharge": df['unnamed.9'],
         "Proportion of TASER ® X26 use - non-discharge": df['unnamed.11'],
         "Drive stun": df['unnamed.12'],
         "Angled drive stun": df['unnamed.14'],
         "Fired": df['unnamed.16'],
         "Total discharge": df['unnamed.18'],
         "Proportion of TASER ® X26 use - discharge": df['unnamed.20'],
         "Not stated": df['unnamed.21'],
         "Total": df['unnamed.23']
         })[2:]
    cleansed.to_csv(os.path.join(directory, filename), index=False)


if __name__ == '__main__':
    save_yearly_sheet()
    save_annual_by_force_sheet(3, 'Table 2: Police use of TASER ® X26 by type, police force and region, 2016',
                               '2016.csv')
    save_annual_by_force_sheet(4, 'Table 3: Revised Police use of TASER ® X26 by type, police force and region, 2015',
                               '2015-revised.csv')
