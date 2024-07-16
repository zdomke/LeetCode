#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    h = int(s[:2])
    h = h % 12 if s[-2] == 'A' else h % 12 + 12
    msec = s[2:8]
    return f"{h:02}{msec}"

    # diff = 12
    # if (s[:2] != '12' and s[-2] == 'A') or (s[:2] == '12' and s[-2] == 'P'):
    #     diff = 0
    # elif s[:2] == '12':
    #     diff = -12
    # ret = str(int(s[:2]) + diff).zfill(2) + s[2:-2]
    # return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
