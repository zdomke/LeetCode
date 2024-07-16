#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringReduction(s):
    # Write your code here
    ch = [s.count('a'), s.count('b'), s.count('c')]
    if ch.count(0) == 2:
        return max(ch)
    mods = [ch[i] % 2 for i in range(3)]
    if mods[0] == mods[1] == mods[2]:
        return 2
    else:
        return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
