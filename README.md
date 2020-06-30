# Resistance Labs Datasets

![Run tests](https://github.com/Resistance-Lab/data/workflows/Run%20tests/badge.svg?branch=trunk)

This repository contains both datasets we have collected as well as scripts used to collect them.

| Output Directory | Description | Source | Script | Last loaded |
| --------------- | ----------- | ------ | ------ | ----------- |
| police-population | Number of police officers per force and per 100,000 population in England and Wales | [1](https://researchbriefings.files.parliament.uk/documents/SN00634/SN00634.pdf) | Manually loaded | 2020-05-14 |
| use-of-force | Police use of force with various breakdowns | [2](https://www.gov.uk/government/statistics/police-use-of-taser-x26-conducted-energy-devices-statistics-england-and-wales-1-january-to-31-december-2016-data-tables), [3](https://www.gov.uk/government/statistics/police-use-of-force-statistics-england-and-wales-april-2017-to-march-2018), [4](https://www.gov.uk/government/statistics/police-use-of-force-statistics-england-and-wales-april-2018-to-march-2019) | scripts/taser_usage | 2020-05-16 |
| demographics | Estimated demographics per area | [5](https://en.wikipedia.org/wiki/Demography_of_Greater_Manchester) | Manually loaded | 2020-05-16 |

## Contributing

If you have relevant datasets then we would like to include them here.  We expect datasets to:

* Be automated where possible, with a script in the `scripts` directory
* Come with [Great Expectations](https://greatexpectations.io/) test suites
* Be documented in the table above

### Great Expectations

You will need a recent version of Python installed to use this.  The rest of the dependencies can then be installed with:

1. Run `python3 -m venv venv && source venv/bin/activate` to create a virtual environment
2. Install the dependencies with `pip3 install -r requirements.txt`
3. Run `great_expectations init` to create any missing directories

To create a test suite for your new dataset run `great_expectations suite new`

To edit a test suite run `great expectations suite edit police-population.warning`

To run the tests and show the results run `great_expectations docs build`
