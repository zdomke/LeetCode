#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    
    st = 0
    en = len(s) - 1
    
    while st < (len(s) / 2):
        if s[st] == s[en]:
            st += 1
            en -= 1
        else:
            if(s[st + 1] == s[en]):
                if(s[st] == s[en - 1] and s[st + 1] == s[en - 2]):
                    return en
                else:
                    return st
            elif s[st] == s[en - 1]:
                return en
    return -1

if __name__ == '__main__':
    print(palindromeIndex('bcbc'))
    print(palindromeIndex('aaab'))
    print(palindromeIndex('aaa'))
    print(palindromeIndex('lfcwnnwcwfl'))