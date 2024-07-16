#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    a = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for c in s:
        upper = c.isupper()
        ind = a.find(c.lower())
        if ind == -1:
            ret += c
            continue
        ind = (ind + k) % 26
        ret += a[ind].upper() if upper else a[ind]
    return ret




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
