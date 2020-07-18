# 2011 Census data by police force area

Author: @WheresAlice

This takes the 2011 Census data on ethnic group and joins it to 2016 ONS stats data mapping local authority to police force area.  The main output is being able to show the total population of different ethnic groups in each police force area.

Whilst we show total populations in this data, it is important to note that they are unlikely to be as accurate as would appear.  There will be some small overlap of local authority areas and police force areas, plus some groups have a history of being underrepresented in census data.

There are also some issues with the source data that you need to be aware of before using this data:

* Ethnicities in the police data are officer-defined, and very limited
* Ethnicities from the census data are self-defined, but still somewhat limited.  The [design of the 2011 census form](https://history.blog.gov.uk/2019/03/07/50-years-of-collecting-ethnicity-data/) will affect people's responses

In both cases, the Asian category is particularly problematic and likely means South Asian in most cases

With these issues noted, the outputs we have are:

## [force-demographics.csv](force-demographics.csv)

shows 2011 census demographics by police force

<iframe style="border-style: none;" src="https://csv.resistancelab.network/#/analysis/0002-demographics-by-police-force-area/force-demographics.csv" height="800" width="900"></iframe>

## [local-authorities-demographics-with-police-force.csv](local-authorities-demographics-with-police-force.csv)

shows 2011 census demographics by local authority, with an extra column for police force

<iframe style="border-style: none;" src="https://csv.resistancelab.network/#/analysis/0002-demographics-by-police-force-area/local-authorities-demographics-with-police-force.csv" height="800" width="900"></iframe>

## [police-defined-demographics.csv](police-defined-demographics.csv)

maps 2011 census demographics to categories used by the police, and is broken down by police force area

<iframe style="border-style: none;" src="https://csv.resistancelab.network/#/analysis/0002-demographics-by-police-force-area/police-defined-demographics.csv" height="800" width="900"></iframe>
