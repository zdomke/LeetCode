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
    sign = {'pos': 0, 'neg': 0, 'zer': 0}

    for num in arr:
        if num > 0:
            sign['pos'] += 1
        elif num < 0:
            sign['neg'] += 1
        else:
            sign['zer'] += 1
    print(f"{(sign['pos'] / len(arr)):.6f}")
    print(f"{(sign['neg'] / len(arr)):.6f}")
    print(f"{(sign['zer'] / len(arr)):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
