from ctrl4bi import cleanser
from ctrl4bi import etl_testing

str1='My DL is A1234567'
print(cleanser.scrub_pii(str1))

import pandas as pd
src_df=pd.read_csv('sample_csv_1.csv')
tgt_df=pd.read_csv('sample_csv_2.csv')
mismatch_count,logs,mismatch_df =etl_testing.column_level_check(src_df,tgt_df,'Identifier')
print('\n'.join(logs))
print(mismatch_df)
