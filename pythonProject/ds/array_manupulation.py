#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
from collections import Counter
def arrayManipulation(n, queries):
    c=Counter()
    for a,b,k in queries:
        c[a]+=k
        c[b]-=k
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    return c[len(c)]

    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
