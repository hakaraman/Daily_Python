"""
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.
"""

import os, re
dir_path = os.path.dirname(os.path.realpath(__file__))
#patern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d|\(\d\d\d\) \d\d\d-\d\d\d')
#with open(dir_path+'/file.txt','r') as f:

import re
with open(dir_path+'/file.txt','r') as f:
#with open('file.txt','r') as f:
    print("".join([i for i in f.readlines() if re.compile(r'\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}').search(i)]))
