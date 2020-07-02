# Resistance Labs Datasets

![Run tests](https://github.com/Resistance-Lab/data/workflows/Run%20tests/badge.svg?branch=trunk)

This repository contains both datasets we have collected as well as scripts used to collect them.

## Datasets in this repository

### Police Population (`police-population`)

Number of police officers per force and per 100,000 population in England and Wales.

| Source | Published | Dates covered | Script | Last loaded |
| -----  | ----------| -------------------- | ------ | ----------- |
| [Police Service Strength (Allen & Audickas) ](https://researchbriefings.files.parliament.uk/documents/SN00634/SN00634.pdf) | 2020-03-04 | 2019-03-31 | Manually loaded | 2020-05-14 |
| [Police workforce, England and Wales (UK Home Office)](https://www.gov.uk/government/statistics/police-workforce-england-and-wales-30-september-2019) | 2020-01-30 | 2018-09-30 - 2019-09-30 | | |

### Taser use (`taser-use`)

> Statistics on police use of TASER X26 conducted energy devices, England and Wales, 2016.

This dataset is the most granular and shows where it has been drawn, arced, red-dotted etc. However it seemingly only exists for this one year, after which it's integrated into the Use of Force data.

| Source | Published | Dates covered | Script | Last loaded |
| -----  | ----------| -------------------- | ------ | ----------- |
| [Police use of TASER ® X26 conducted energy devices statistics, England and Wales: 1 January to 31 December 2016: data tables, UK Home Office](https://www.gov.uk/government/statistics/police-use-of-taser-x26-conducted-energy-devices-statistics-england-and-wales-1-january-to-31-december-2016-data-tables) | 2017-04-13 | 2016-01-01 - 2016-12-31 |

### Use of force (`use-of-force`)

> Statistics on incidents where police officers use force; including type of force, reason, outcome, injuries, and subject information (such as age, gender).

This has actual taser information in a simpler format (just drawn and fired), but seems to be the new reporting format that will be used in perpetuity. It has it's own [user guide](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/763512/user-guide-police-use-of-force.pdf) which is a **must read** to understand this data.

| Source | Published | Dates covered | Script | Last loaded |
| -----  | ----------| -------------------- | ------ | ----------- |
| [Police use of force statistics, England and Wales: April 2017 to March 2018, UK Home Office](https://www.gov.uk/government/statistics/police-use-of-force-statistics-england-and-wales-april-2017-to-march-2018) | 2018-12-13 | 2017-04-01 - 2018-03-31
| [Police use of force statistics, England and Wales: April 2018 to March 2019, UK Home Office](https://www.gov.uk/government/statistics/police-use-of-force-statistics-england-and-wales-april-2018-to-march-2019) | 2019-12-19 | 2018-04-01 - 2019-03-31 | |

### UK Demographics (`demographics`)

Demographic information is sourced from the 2011 UK Census via the "nomisweb" service.

> This dataset provides 2011 estimates that classify usual residents in England and Wales by ethnic group. The ethnic group classification used is the standard 18-category classification corresponding to the tick box response options on the census questionnaire. The estimates are as at census day, 27 March 2011.

| Source | Published | Dates covered | Script | Last loaded |
| -----  | ----------| -------------------- | ------ | ----------- |
| [Census 2011: Ethnic group, Nomis official labour market statistics](https://www.nomisweb.co.uk/census/2011/qs201ew) | 2013-01-30 | 2011 | | |


## Contributing

If you have relevant datasets then we would like to include them here. We expect datasets to:

* Be automated where possible, with a script in the `scripts` directory
* Come with [Great Expectations](https://greatexpectations.io/) test suites
* Be documented in the table above

Feel free to open a ticket or email [kim@resistancelab.network](mailto:kim@resistancelab.network) with any questions.

### Testing

Tests are provided using Great Expectations. You will need a recent version of Python installed to use this.  The rest of the dependencies can then be installed with:

1. Run `python3 -m venv venv && source venv/bin/activate` to create a virtual environment
2. Install the dependencies with `pip3 install -r requirements.txt`
3. Run `great_expectations init` to create any missing directories

To create a test suite for your new dataset run `great_expectations suite new`

To edit a test suite run `great expectations suite edit police-population.warning`

To run the tests and show the results run `great_expectations docs build`
