# flake8: noqa
import pandas as pd
import os

repo_root = os.path.join(os.path.dirname(__file__), '..', '..')

demographics = pd.read_csv(os.path.join(repo_root, 'source_data', 'demographics', 'la-ethnic-groups.csv'))
la_to_police_force = pd.read_csv(os.path.join(repo_root, 'source_data', 'demographics',
                                              'Local_Authority_District_to_Community_Safety_Partnerships_to_Police_Force_Areas__December_2016__Lookup_in_England_and_Wales.csv'))

enriched_demographics = demographics.set_index('geography code').join(la_to_police_force.set_index('LAD16CD'))
enriched_demographics['geography'] = enriched_demographics['geography'].str.replace('Avon and Somerset',
                                                                                    'Avon & Somerset')
enriched_demographics['geography'] = enriched_demographics['geography'].str.replace('London, City of', 'City of London')
enriched_demographics['geography'] = enriched_demographics['geography'].str.replace('Metropolitan Police',
                                                                                    'Metropolitan')

enriched_demographics['PFA16NM'] = enriched_demographics['PFA16NM'].str.replace('Avon and Somerset', 'Avon & Somerset')
enriched_demographics['PFA16NM'] = enriched_demographics['PFA16NM'].str.replace('London, City of', 'City of London')
enriched_demographics['PFA16NM'] = enriched_demographics['PFA16NM'].str.replace('Metropolitan Police', 'Metropolitan')

enriched_demographics.to_csv('local-authorities-demographics-with-police-force.csv', index=False)

# group by police force
force_demographics = enriched_demographics.groupby(['PFA16NM']).sum().drop(['date', 'FID'], axis=1)
force_demographics.to_csv('force-demographics.csv', index=True)

# map to police ethnicity definitions

police_demographics = pd.DataFrame({
    "Police force": force_demographics.index,
    "White": force_demographics['Ethnic Group: White; measures: Value'],
    "Black (or Black British)": force_demographics['Ethnic Group: Black; measures: Value'],
    "Asian (or Asian British)": force_demographics['Ethnic Group: Asian/Asian British: Indian; measures: Value'] +
                                force_demographics['Ethnic Group: Asian/Asian British: Pakistani; measures: Value'] +
                                force_demographics['Ethnic Group: Asian/Asian British: Bangladeshi; measures: Value'] +
                                force_demographics['Ethnic Group: Asian/Asian British: Other Asian; measures: Value'],
    "Chinese": force_demographics['Ethnic Group: Asian/Asian British: Chinese; measures: Value'],
    "Mixed": force_demographics['Ethnic Group: Mixed; measures: Value'],
    "Other": force_demographics['Ethnic Group: Other; measures: Value']
})

police_demographics.to_csv('police-defined-demographics.csv', index=False)
