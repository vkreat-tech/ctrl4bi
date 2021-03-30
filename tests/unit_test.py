from ctrl4bi import cleanser
from ctrl4bi import etl_testing
from ctrl4bi import datasets
from ctrl4bi import data_wrangling

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people_flattened=data_wrangling.flatten_dict(people)
print(people_flattened)
