#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    ind = 0
    w = [1, 2, 3]
    for val in q:
        if val not in w:
            print("Too chaotic")
            return
        ind = w.index(val)
        bribes += ind
        w.append(w[-1] + 1)
        w.pop(ind)
    print(bribes)
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
