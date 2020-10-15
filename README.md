# Ctrl4BI 
[![Downloads](http://pepy.tech/badge/ctrl4bi)](http://pepy.tech/project/ctrl4bi)

#### This is a helper package for Business Intelligence solutions.

For documentation, please read [HELP.md](https://github.com/vkreat-tech/ctrl4bi/blob/master/HELP.md)

For demo on usage, please check [README.ipynb](https://github.com/vkreat-tech/ctrl4bi/blob/master/README.ipynb)


#### Contact Developer: [Shaji](https://www.linkedin.com/in/shaji-james/)

## Highlights
- PII scrubbing
- ETL testing - Column Level Check

## Dependencies

Ctrl4BI requires:

* Python (tested under Python 3.8)

## Installation

The easiest way to install the latest release version of Ctrl4BI is via ```pip```:
```bash
pip install ctrl4bi
```
In case you get ```ERROR: Could not install packages due to an EnvironmentError```, try using
```bash
pip install ctrl4bi --user
```
Check for the latest available version in [Ctrl4BI](https://pypi.org/project/ctrl4bi/)

## Import

Import any module from the package thru the following method:
```bash
from ctrl4bi import cleanser
```
```bash
from ctrl4bi import etl_testing
```

## Learn to use

Understand what each functions does by using ```help()```:
```bash
help(cleanser.scrub_pii)
```

## ChangeLog

This is the first official release of the package

## ToDo

- Data Wrangling
- Relationalize Unstructured Data
