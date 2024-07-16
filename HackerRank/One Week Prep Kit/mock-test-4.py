#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    start = 0
    passed = 0
    fuel = 0
    while passed < len(petrolpumps):
        pump = petrolpumps.pop(0)
        fuel += pump[0]
        if fuel >= pump[1]:
            passed += 1
            fuel -= pump[1]
        else:
            start += passed + 1
            passed = 0
            fuel = 0
        petrolpumps.append(pump)
    print(start)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
