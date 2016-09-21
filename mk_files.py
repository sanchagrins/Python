#!/usr/bin/env python
#
# Author: Stephen Sanchagrin
# Title: mk_files.py
# Date: 9/21/2016
# Description: Makes a a given number of empty files in the
#              current working directory. Useful for generating
#              test files for scripting exercises.
#

import os

def padding(num_len, count): # Calculates padding for file numbers
    count_len = len(str(count))
    pad_len = num_len - count_len
    zeros = ("0"*pad_len)
    return zeros

pad = 0
num = raw_input("Enter number of files to generate: ")
num_int = int(num)
if num > 0:
    count = 1
    num_len = len(str(num))
    while (count <= num_int):
        pad = padding(num_len, count)
        file_name = "file_" + pad +  str(count) + ".txt"
        print(" Generating " + file_name + "...")
        new_file = open(file_name,'a+')
        count = count + 1
else:
    print("Invalid number.")
print(num + " files generated.")
