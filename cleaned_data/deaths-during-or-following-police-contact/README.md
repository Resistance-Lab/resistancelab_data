This data comes from the ODS spreadsheet, [Time_series_tables_2018-19.ods](https://policeconduct.gov.uk/sites/default/files/Documents/statistics/Time_series_tables_2018-19.ods), from [here](https://policeconduct.gov.uk/research-and-learning/statistics/annual-deaths-during-or-following-police-contact-statistics).  The raw data has multiple tables in some sheets, and the website blocks the download of this file in automated manner.  So the data has been transposed manually.  We have saved a copy of the source spreadsheet in the [source_data](../../source_data/deaths-during-or-following-police-contact/Time_series_tables_2018-19.ods)

The data itself isn't entirely accurate, due to a number of incidents still being under investigation, and some cross-over between multiple forces.  The original source spreadsheet explains this.

The following tables are available:

- [deaths in or following police custody](custody_by_force/fatalities.csv)
- [road traffic incidents](rti_by_force/incidents.csv)
- [road traffic fatalities](rti_by_force/fatalities.csv)
- [fatal shootings](shootings_by_force/fatalities.csv)
- [apparent suicides following police custody](suicides_by_force/fatalities.csv)
- [other deaths following police contact](other_contact_by_force/fatalities.csv)
- [incidents involving other deaths following police contact](other_contact_by_force/incidents.csv)

In addition to the standard list of regional forces that we use throughout this repository, this data also includes data for the following non-regional forces:

- British Transport
- HMRC
- Home Office
- Ministry of Defence
- SOCA / NCA
