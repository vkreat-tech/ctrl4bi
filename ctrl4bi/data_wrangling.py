# -*- coding: utf-8 -*-
"""
About Ctrl4BI
    Open Source Project Developed by VKreaT (www.vkreat.com)
    Ctrl4BI has automated methods to automate Business Intelligence solutions

About ctrl4bi.data_wrangling
    The module has functions that has functions to parse data of multiple formats and convert them to relational format

Last Updated On: 14 Feb 2023
"""

import pandas as pd
import json

def read_vcf(input_file,output_file=None):
    """
    Usage: [arg1]:[Input File] [arg2]:[Output File - Optional Parameter (The return dataframe will be written to csv if output path is specified)]
    Description: Reads the vcf file and returns the name, phone numbers and email as DataFrame
    Returns: [Dataframe of name, phone numbers and email]
    """
    contacts=[]
    def require(line):
        if line[:3]=='FN:':
            return True
        elif line[:4]=='TEL;':
            return True
        elif line[:6]=='EMAIL;':
            return True
        else:
            return False
    def incr_key(key):
        key_split=key.split('_')
        curr=int(key_split[-1])
        key_split[-1]=str(curr+1)
        return '_'.join(key_split)
    with open(input_file, 'r') as f:
        contact=dict()
        for line in f:
            if line[:9]!='END:VCARD':
                if require(line):
                    line_split=line.split(':')
                    key=line_split[0]
                    value=line_split[1]
                    value=str(value).strip()
                    if key=='FN':
                        contact['Name']=value
                    else:
                        key=key.replace(';', '_')
                        key=key+'_1'
                        if key in contact.keys():
                            key=incr_key(key)
                        value=value.replace('+91', '(+)91-')
                        contact[key]=value
            else:
                contacts.append(contact)
                contact=dict()
    df = pd.DataFrame(contacts)
    if output_file:
        df.to_csv(output_file)
    return df


def flatten_dict(y):
    """
    Usage: [arg1]:[Nested Dictionary]
    Description: Flattens the dictionary, elements in List type with be give unique numbers
    Returns: [Flat Dictionary]
    """
    out = {}
    def flatten(x, name =''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + str(a) + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(str(a), name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

def flatten_json(json_str):
    """
    Usage: [arg1]:[Nested JSON string]
    Description: Flattens the JSON, elements in JSON Array type with be give unique numbers
    Returns: [Flat JSON string]
    """
    json_dict=json.loads(json_str)
    flat_dict=flatten_dict(json_dict)
    flat_json=json.dumps(flat_dict)
    return flat_json
