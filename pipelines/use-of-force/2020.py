import pandas as pd
from pandas_ods_reader import read_ods
import os
from utils import download, make_output_directory


def save_sheet(sheet, title, year, filename):
    directory = make_output_directory("by-ced-type-force-region")
    df = read_ods(output_file, sheet)

    # Drop the empty rows
    df.drop([0, 1, 165, 166, 167, 168, 169], inplace=True)

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


def save_health_condition():
    directory = make_output_directory("by-health-condition-force")
    df = read_ods(output_file, "Table_17")
    df.drop([0, 1, 2, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684], inplace=True)
    # print(df)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 17. Number of times tactics were used, by police force and officer perceived health condition of person involved, year ending March 2020'].str.strip(),
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
    for i in ['Mental', 'Physical', 'Physical and mental', 'None', 'Not reported', 'Number of times tactic reported']:
        cleansed[i] = cleansed[i].apply(pd.to_numeric, errors='coerce')
    cleansed.to_csv(os.path.join(directory, 'april2019-march2020.csv'), index=False)


def save_ethnicity():
    directory = make_output_directory("by-ethnicity-force")
    df = read_ods(output_file, "Table_16")
    df.drop([0, 1, 2, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684], inplace=True)
    # print(df)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 16. Number of times tactics were used, by police force and officer perceived ethnicity of person involved, year ending March 2020'].str.strip(),
            "Type of force": df['unnamed.1'],
            "Tactic": df['unnamed.2'],
            "White": df['unnamed.3'],
            "Black (or Black British)": df['unnamed.4'],
            "Asian (or Asian British)": df['unnamed.5'],
            "Mixed": df['unnamed.6'],
            "Other": df['unnamed.7'],
            "Not reported": df['unnamed.8'],
            "Number of times tactic reported": df['unnamed.9']
        }
    )[1:]
    cleansed['Tactic'] = cleansed['Tactic'].str.replace(r'\d+', '')
    # Some columns have ':' to represent not available, so coerce to numeric
    for i in ['White', 'Black (or Black British)', 'Asian (or Asian British)', 'Mixed', 'Other', 'Not reported', 'Number of times tactic reported']:
        cleansed[i] = cleansed[i].apply(pd.to_numeric, errors='coerce')
    cleansed.to_csv(os.path.join(directory, 'april2019-march2020.csv'), index=False)


def save_age():
    directory = make_output_directory("by-age-force")
    df = read_ods(output_file, "Table_14")
    df.drop([0, 1, 2, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684], inplace=True)
    # print(df)
    cleansed = pd.DataFrame(
        {
            "Police Force": df[
                'Table 14. Number of times tactics were used, by police force and officer perceived age of person involved, year ending March 2020'].str.strip(),
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
    for i in ['Under 11 years', '11 - 17 years', '18 - 34 years', '35 - 49 years', '50 - 64 years', '65 and over', 'Not reported', 'Number of times tactic reported']:
        cleansed[i] = cleansed[i].apply(pd.to_numeric, errors='coerce')
    cleansed.to_csv(os.path.join(directory, 'april2019-march2020.csv'), index=False)


def save_incidents():
    directory = make_output_directory("incidents")
    df = read_ods(output_file, "Table_12")
    df.drop([0, 1, 2], inplace=True)
    # print(df)
    cleansed = pd.DataFrame(
        {
            "Region": df['Table 12. Incidents by police force, year ending March 2020'],
            "Police Force": df['unnamed.1'],
            "Total": df['unnamed.2']
        }
    )
    cleansed['Total'] = cleansed['Total'].apply(pd.to_numeric, errors='coerce')
    cleansed.to_csv(os.path.join(directory, "april2019-march2020.csv"), index=False)


if __name__ == '__main__':
    # Download the file into the raw directory
    ods_file_2020 = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/944989/police-use-of-force-apr2019-mar2020-hosb3720-tables.ods'
    output_file = download(ods_file_2020)

    save_sheet('Table_13', 'Table 13. Use of CED by type and police force: 1 April 2017 to 31 March 2020', '2019/20',
               'april2019-march2020.csv')
    save_health_condition()
    save_ethnicity()
    save_age()
    save_incidents()
