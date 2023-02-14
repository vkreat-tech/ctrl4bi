# -*- coding: utf-8 -*-
"""
About Ctrl4BI
    Open Source Project Developed by VKreaT (www.vkreat.com)
    Ctrl4BI has automated methods to automate Business Intelligence solutions

About ctrl4bi.etl_testing
    The module has functions to do data validations between source and target

Last Updated On: 14 Feb 2023
"""

from . import exceptions

from datetime import datetime
import os
import pandas as pd

def column_level_check(source_df,target_df,primary_keys):
    """
    Usage: [arg1]:[Pandas DataFrame - source], [arg2]:[Pandas DataFrame - target], [arg3]:[Primary keys (separated by comma)]
    Description: Performs column level testing between two DataFrames by joining using the primary keys.
    Returns: [Mismatch Count], [Test Log (list)], [Pandas dataframe - mismatch (if any)]
    """
    global execution_status

    systime=datetime.now()

    start_time=systime.strftime("%Y")+'-'+systime.strftime("%m")+'-'+systime.strftime("%d")+' '+systime.strftime("%H")+':'+systime.strftime("%M")+':'+systime.strftime("%S")

    log_list=[]

    execution_status='RUNNING'

    log_list.append('START TIME: '+start_time)

    key_list=primary_keys.split(',')

    src=source_df
    tgt=target_df

    log_list.append(str(datetime.now())+': DIFFERENTIATING SOURCE AND TARGET COLUMNS')
    if execution_status!='FAILED':
        try:
            src_k=[]
            src_columns=[]
            for i  in src.columns:
                if str.lower(i) in [str.lower(key) for key in key_list]:
                    src_columns.append(str.lower(i))
                    src_k.append(str.lower(i))
                else:
                    src_columns.append(str(i) + '_src')
            src.columns = src_columns
            tgt_k=[]
            tgt_columns=[]
            for i  in tgt.columns:
                if str.lower(i) in [str.lower(key) for key in key_list]:
                    tgt_columns.append(str.lower(i))
                    tgt_k.append(str.lower(i))
                else:
                    tgt_columns.append(str(i) + '_tgt')
            tgt.columns = tgt_columns
        except Exception as e:
            print('Failed while DIFFERENTIATING SOURCE AND TARGET COLUMNS: '+str(e))
            log_list.append('Failed while DIFFERENTIATING SOURCE AND TARGET COLUMNS: '+str(e))
            execution_status='FAILED'
    log_list.append(str(datetime.now())+': CHECKING IF THE GROUP BY MAKES THE RECORD LEVEL SAME AS ACTUAL')
    if execution_status!='FAILED':
        try:
            index_unique_flag=[]
            if src.groupby(src_k).count().shape[0]==src.shape[0]:
                index_unique_flag.append(True)
            else:
                index_unique_flag.append(False)
            if tgt.groupby(tgt_k).count().shape[0]==tgt.shape[0]:
                index_unique_flag.append(True)
            else:
                index_unique_flag.append(False)
        except Exception as e:
            print('Failed while CHECKING IF THE GROUP BY MAKES THE RECORD LEVEL SAME AS ACTUAL: '+str(e))
            log_list.append('Failed while CHECKING IF THE GROUP BY MAKES THE RECORD LEVEL SAME AS ACTUAL: '+str(e))
            execution_status='FAILED'
    if execution_status!='FAILED':
        try:
            if all(index_unique_flag)==True:
                log_list.append(str(datetime.now())+': JOINING THE TABLES')
                try:
                    df=tgt.set_index(tgt_k).join(src.set_index(src_k),how='left')
                except Exception as e:
                    print('Failed while JOINING THE TABLES: '+str(e))
                    log_list.append('Failed while JOINING THE TABLES: '+str(e))
                    execution_status='FAILED'
                log_list.append(str(datetime.now())+': FINDING THE TARGET COLUMN AND SOURCE COLUMN TO BE COMPARED')
                if execution_status!='FAILED':
                    try:
                        ma_list=[]
                        for i in range(len(df.columns)):
                            if df.columns[i][-3:]=='tgt':
                                for j in range(len(df.columns)):
                                    if df.columns[j][-3:]=='src':
                                        if str.lower(df.columns[i][:-4])==str.lower(df.columns[j][:-4]):
                                            ma_list.append([j,i])
                        match_cols=''
                        for i in range(len(ma_list)):
                            match_cols+=str(i+1)+': '+df.columns[ma_list[i][1]]+' = '+df.columns[ma_list[i][0]]+' , '
                        log_list.append('Matching columns '+match_cols)
                    except Exception as e:
                        print('Failed while FINDING THE TARGET COLUMN AND SOURCE COLUMN TO BE COMPARED: '+str(e))
                        log_list.append('Failed while FINDING THE TARGET COLUMN AND SOURCE COLUMN TO BE COMPARED: '+str(e))
                        execution_status='FAILED'
                log_list.append(str(datetime.now())+': COMPARISION STARTED')
                if execution_status!='FAILED':
                    try:
                        mis_cols=[]
                        res=[]
                        index=[]
                        for i in range(len(ma_list)):
                            if all(df[df.columns[ma_list[i][0]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0))==df[df.columns[ma_list[i][1]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0)))==True:
                                res.append(True)
                            else:
                                res.append(False)
                                mis_cols.append(df.columns[ma_list[i][0]])
                                mis_cols.append(df.columns[ma_list[i][1]])
                                for j in range(len(df[df.columns[ma_list[i][0]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0))==df[df.columns[ma_list[i][1]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0)))):
                                    if list(df[df.columns[ma_list[i][0]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0))==df[df.columns[ma_list[i][1]]].apply(lambda x:str(x).strip()).astype(str).fillna(str(0)))[j]==False:
                                        index.append(j)
                        un_df=df[mis_cols].iloc[list(set(index))]
                    except Exception as e:
                        print('Failed while COMPARING: '+str(e))
                        log_list.append('Failed while COMPARING: '+str(e))
                        execution_status='FAILED'
                log_list.append(str(datetime.now())+': TEST RESULT:')
                if execution_status!='FAILED':
                    try:
                        if all(res)==True:
                            mismatch_count=0
                            print('COLUMN LEVEL CHECK PASSED')
                            execution_status='SUCCESS'
                            log_list.append('COLUMN LEVEL CHECK PASSED')
                        else:
                            log_list.append((str(len(set(index)))+' records unmatched'))
                            log_list.append('Column level check Failed')
                            mismatch_count=str(len(set(index)))
                            execution_status='SUCCESS'
                    except Exception as e:
                        print('Failed while getting the TEST RESULT: '+str(e))
                        log_list.append('Failed while getting the TEST RESULT: '+str(e))
                        execution_status='FAILED'
            else:
                log_list.append('The records grouped at the level of key columns are not unique')
        except Exception as e:
            log_list.append('Failed while CHECKING IF THE GROUP BY MAKES THE RECORD LEVEL SAME AS ACTUAL: '+str(e))
            execution_status='FAILED'
    if execution_status=='FAILED':
        print('Check Logs for the error message')
        raise exceptionsExecutionError
    return mismatch_count,log_list,un_df

def sort_and_compare(source_df,target_df):
    """
    Usage: [arg1]:[Pandas DataFrame - source], [arg2]:[Pandas DataFrame - target]
    Description: Sort and Compare two datasets.
    Returns: [Mismatch Count], [Test Log (list)], [Pandas dataframe - mismatch (if any)]
    """
    for col in source_df.columns:
        source_df[col] = source_df[col].apply(lambda x:str(x).strip()).astype(str).fillna(str(0))
    for col in target_df.columns:
        target_df[col] = target_df[col].apply(lambda x:str(x).strip()).astype(str).fillna(str(0))
    log_list=[]
    col1=source_df.columns
    col2=target_df.columns
    cols=list(set(col1.sort_values()).intersection(set(col2.sort_values())))
    log_list.append('Common column(s): '+', '.join(cols))

    source_df.sort_values(cols, axis=0, ascending=True, inplace=True)
    target_df.sort_values(cols, axis=0, ascending=True, inplace=True)

    data1=source_df[cols].reset_index(drop=True)
    data2=target_df[cols].reset_index(drop=True)

    data1.head()
    data2.head()

    result=data1==data2
    bool_list=[]
    mis_cols=[]
    mis_index=[]
    for i in cols:
        if all(result[i])==True:
            bool_list.append(True)
        else:
            bool_list.append(False)
            mis_cols.append(i)
            for j in range(len(result[i])):
                if result[i][j]==False:
                    mis_index.append(j)
    un_df=pd.concat([data1.iloc[list(set(mis_index))],data2.iloc[list(set(mis_index))]],axis=1)

    mismatch_count=0
    if all(bool_list)==True:
        log_list.append('Records are matching')
    else:
        mismatch_count=len(set(mis_index))
        log_list.append(str(mismatch_count)+' records unmatched')
        log_list.append('Column(s): '+', '.join(mis_cols))
    return mismatch_count,log_list,un_df[mis_cols]
