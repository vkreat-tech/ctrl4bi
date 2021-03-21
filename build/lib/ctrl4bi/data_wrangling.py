# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:18:10 2020

@author: Shaji
"""

import pandas as pd

def read_vcf(input_file,output_file=None):
    """
    Usage: [arg1]:[Input File] [arg1]:[Output File - Optional Parameter (The return dataframe will be written to csv if output path is specified)]
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
