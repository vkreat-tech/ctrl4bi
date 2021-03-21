from ctrl4bi import cleanser
from ctrl4bi import etl_testing
from ctrl4bi import datasets

str1='My DL is A1234567'
print(cleanser.scrub_pii(str1))

src_df,tgt_df=datasets.clc_samples(refresh=True)

mismatch_count,logs,mismatch_df =etl_testing.sort_and_compare(src_df,tgt_df)
print('\n'.join(logs))
print(mismatch_df)
