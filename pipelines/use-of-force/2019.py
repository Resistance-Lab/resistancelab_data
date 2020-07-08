import pandas as pd
from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory


# Obviously this is in yet a different format to the previous year, so we can't just re-use in a library
def save_sheet(sheet, title, year, filename):
    directory = make_output_directory("by-ced-type-force-region")
    df = read_ods(output_file, sheet)

    # Drop the empty rows
    df.drop([0, 1, 57, 58, 59, 60, 61], inplace=True)

    # Build a new dataframe with correct column names
    cleansed = pd.DataFrame(
        {
            "Financial Year": df[title],
            "Region": df['unnamed.1'],
            "Police force": df['unnamed.2'].str.replace("\(.+\)", "", regex=True).str.strip(),  # noqa: W605
            "Total": df['unnamed.3'],
            "Total non-discharge": df['unnamed.4'],
            "Drawn": df['unnamed.5'],
            "Aimed": df['unnamed.6'],
            "Red-dot": df['unnamed.7'],
            "Arced": df['unnamed.8'],
            "Total discharge": df['unnamed.9'],
            "Drive stun": df['unnamed.10'],
            "Fired": df['unnamed.11'],
            "Angled drive stun": df['unnamed.12'],
            "Not stated": df['unnamed.13']})[1:]

    # Write to file
    cleansed[cleansed['Financial Year'] == year].drop(columns=['Financial Year']).to_csv(
        os.path.join(directory, filename), index=False)


def save_disability():
    directory = make_output_directory("by-disability-force")
    df = read_ods(output_file, "Table_17")
    df.drop([0, 1, 2, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553], inplace=True)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 17. Number of times tactics were used, by police force and officer perceived disability of subject'].str.strip(),
            "Type of force": df['unnamed.1'],
            "Tactic": df['unnamed.2'],
            "Mental": df['unnamed.3'],
            "Physical": df['unnamed.4'],
            "Physical and mental": df['unnamed.5'],
            "None": df['unnamed.6'],
            "Not reported": df['unnamed.7'],
            "Number of times tactic reported": df['unnamed.8']
        }
    )[1:]
    cleansed['Tactic'] = cleansed['Tactic'].str.replace(r'\d+', '')
    cleansed.to_csv(os.path.join(directory, 'april2018-march2019.csv'), index=False)


def save_ethnicity():
    directory = make_output_directory("by-ethnicity-force")
    df = read_ods(output_file, "Table_16")
    df.drop([0, 1, 2, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552], inplace=True)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 16. Number of times tactics were used, by police force and officer perceived ethnicity of subject'].str.strip(),
            "Type of force": df['unnamed.1'],
            "Tactic": df['unnamed.2'],
            "White": df['unnamed.3'],
            "Black (or Black British)": df['unnamed.4'],
            "Asian (or Asian British)": df['unnamed.5'],
            "Chinese": df['unnamed.6'],
            "Mixed": df['unnamed.7'],
            "Other": df['unnamed.8'],
            "Don't know": df['unnamed.9'],
            "Not reported": df['unnamed.10'],
            "Number of times tactic reported": df['unnamed.11']
        }
    )[1:]
    cleansed['Tactic'] = cleansed['Tactic'].str.replace(r'\d+', '')
    cleansed.to_csv(os.path.join(directory, 'april2018-march2019.csv'), index=False)


def save_age():
    directory = make_output_directory("by-age-force")
    df = read_ods(output_file, "Table_14")
    df.drop([0, 1, 2, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553], inplace=True)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 14. Number of times tactics were used, by police force and officer perceived age of subject'].str.strip(),
            "Type of force": df['unnamed.1'],
            "Tactic": df['unnamed.2'],
            "Under 11 years": df['unnamed.3'],
            "11 - 17 years": df['unnamed.4'],
            "18 - 34 years": df['unnamed.5'],
            "35 - 49 years": df['unnamed.6'],
            "50 - 64 years": df['unnamed.7'],
            "65 and over": df['unnamed.8'],
            "Not reported": df['unnamed.9'],
            "Number of times tactic reported": df['unnamed.10']
        }
    )[1:]
    cleansed['Tactic'] = cleansed['Tactic'].str.replace(r'\d+', '')
    cleansed.to_csv(os.path.join(directory, 'april2018-march2019.csv'), index=False)


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
    cleansed.to_csv(os.path.join(directory, "april2018-march2019.csv"), index=False)


if __name__ == '__main__':
    # Download the file into the raw directory
    ods_file_2019 = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/852998/police-use-of-force-apr2018-mar2019-hosb3319-tables.ods'
    output_file = download(ods_file_2019)

    save_sheet('Table_13', 'Table 13. Use of CED by type and police force: 1 April 2017 to 31 March 2019', '2017/18',
               'april2017-march2018.csv')
    save_sheet('Table_13', 'Table 13. Use of CED by type and police force: 1 April 2017 to 31 March 2019', '2018/19',
               'april2018-march2019.csv')
    save_disability()
    save_ethnicity()
    save_age()
    save_incidents()
