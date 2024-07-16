#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    if k == len(n) == 1: return int(n)
    run = sum([int(c) for c in n])
    return superDigit(str(run * k), 1)

    n = n * k
    if len(n) == 1:
        return int(n)
    run = sum([int(c) for c in n])
    return superDigit(str(run), 1)


if __name__ == '__main__':
    print(superDigit("9875", 1))
    print(superDigit("9875", 4))
