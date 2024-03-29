# -*- coding: utf-8 -*-
"""
About Ctrl4BI
    Open Source Project Developed by VKreaT (www.vkreat.com)
    Ctrl4BI has automated methods to automate Business Intelligence solutions

About ctrl4bi.datasets
    The module has practice datasets which can used by unit tests or to practice different functionalities

Last Updated On: 14 Feb 2023
"""

import pandas as pd
import requests
import os

pd.set_option('mode.chained_assignment', None)

def clc_samples(refresh=False):
  """
  Usage: [arg1]:[refresh=False(default)/True - True if the file should be downloaded and refreshed again from intenet]
  Description: Sample dataframes for demonstrating Column Level Check
  Primary Key: Identifier
  Returns: [DataFrame 1], [DataFrame 2 (with mismatch)]
  """
  if (not os.path.exists('sample_csv_1.csv')) or (refresh==True):
    print('Downloading sample_csv_1.csv ......')
    df1_request = requests.get("https://github.com/vkreat-tech/ctrl4bi/raw/master/sample_datasets/sample_csv_1.csv", allow_redirects=True)
    open('sample_csv_1.csv', 'wb').write(df1_request.content)
  df1=pd.read_csv('sample_csv_1.csv')
  if (not os.path.exists('sample_csv_2.csv')) or (refresh==True):
    print('Downloading sample_csv_2.csv ......')
    df2_request = requests.get("https://github.com/vkreat-tech/ctrl4bi/raw/master/sample_datasets/sample_csv_2.csv", allow_redirects=True)
    open('sample_csv_2.csv', 'wb').write(df2_request.content)
  df2=pd.read_csv('sample_csv_2.csv')
  return df1,df2


