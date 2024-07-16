#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = {'pos': 0, 'neg': 0, 'zer': 0}
    for a in arr:
        if a > 0:
            count['pos'] += 1
        elif a < 0:
            count['neg'] += 1
        else:
            count['zer'] += 1
    print(f"{(count['pos'] / len(arr)):6}")
    print(f"{(count['neg'] / len(arr)):6}")
    print(f"{(count['zer'] / len(arr)):6}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
