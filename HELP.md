# ctrl4bi.aws_connect

##    download_dir(bucket, prefix, local_path, client=<botocore.client.S3 object>)
        Usage: [arg1]:[bucket name],[arg2]:[pattern to match keys in s3],[arg3]:[local path to folder in which to place files],[arg4]:[initialized s3 client object],
        Description: Downloads the contents to the local path
    
##    list_buckets(client=<botocore.client.S3 object>)
        Usage: [arg1]:[initialized s3 client object],
        Description: Gets the list of buckets
        Returns: [list of buckets]
    
##    list_objects(bucket, prefix='', client=<botocore.client.S3 object>)
        Usage: [arg1]:[bucket name],[arg2]:[pattern to match keys in s3],[arg3]:[initialized s3 client object],
        Description: Gets the keys in the S3 location
        Returns: [list of keys], [list of directories]


# ctrl4bi.cleanser

##    scrub_pii(string)
        Usage: [arg1]:[String with PII]
        Description: Removes PII content from string. Be careful while performing this as this would remove even anything that looks like PII
        Returns: [String without PII]


# ctrl4bi.etl_testing		

##    column_level_check(source_df, target_df, primary_keys)
        Usage: [arg1]:[Pandas DataFrame - source], [arg2]:[Pandas DataFrame - target], [arg3]:[Primary keys (separated by comma)]
        Description: Performs column level testing between two DataFrames.
        Returns: [Mismatch Count], [Test Log (list)], [Pandas dataframe - mismatch (if any)]
    
##    sort_and_compare(source_df, target_df)
        Usage: [arg1]:[Pandas DataFrame - source], [arg2]:[Pandas DataFrame - target]
        Description: Sort and Compare two datasets.
        Returns: [Mismatch Count], [Test Log (list)], [Pandas dataframe - mismatch (if any)]


#    ctrl4bi.datasets

##    clc_samples()
        Description: Sample dataframes for demonstrating Column Level Check
        Primary Key: Identifier
        Returns: [DataFrame 1], [DataFrame 2 (with mismatch)]

