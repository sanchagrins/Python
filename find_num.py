#!/usr/bin/env python
# Purpose: Exercise for Coursera Class Using Python to Access Web Data.
#          Reads through a file, extracts numbers using regex and sums them.

import re

fh = open("regex_sum_320787.txt", 'r')
numlist = list()
for line in fh: 
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if x:
        x = [int(i) for i in x]
        numlist.extend(x)
print sum(numlist)
