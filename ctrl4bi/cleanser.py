# -*- coding: utf-8 -*-
"""
About Ctrl4BI
    Open Source Project Developed by VKreaT (www.vkreat.com)
    Ctrl4BI has automated methods to automate Business Intelligence solutions

About ctrl4bi.cleanser
    The module has functions that does data pre-processing

Last Updated On: 14 Feb 2023
"""

import re

def scrub_pii(string):
    """
    Usage: [arg1]:[String with PII]
    Description: Removes PII content from string. Be careful while performing this as this would remove even anything that looks like PII
    Returns: [String without PII]
    """
    patterns=[]
    patterns.append(r'(?![a-zA-Z-\.]{6,30})[a-zA-Z0-9-\.]{6,30}')
    patterns.append(r'((?![a-zA-Z]{2,15})[a-zA-Z0-9]{2,15} +){2,}')
    string=' '+str(string)+' '
    string=string.replace('\\"',' \\" ')
    for pattern in patterns:
        regexPattern=re.compile(pattern)
        string=re.sub(regexPattern,' --- PII SCRUBBED ---- ',string)
    string=string.replace(' \\" ','\\"')
    return str.strip(string)
