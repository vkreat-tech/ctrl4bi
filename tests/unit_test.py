from ctrl4bi import cleanser
from ctrl4bi import etl_testing
from ctrl4bi import datasets

str1='My DL is A1234567'
print(cleanser.scrub_pii(str1))

src_df,tgt_df=datasets.clc_samples()
mismatch_count,logs,mismatch_df =etl_testing.column_level_check(src_df,tgt_df,'Identifier')
print('\n'.join(logs))
print(mismatch_df)

