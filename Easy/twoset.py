#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    # LCM of array a
    l = a[0]
    for x in a[1:]:
        l = lcm(l, x)

    # GCD of array b
    g = b[0]
    for x in b[1:]:
        g = gcd(g, x)

    count = 0
    multiple = l

    while multiple <= g:
        if g % multiple == 0:
            count += 1
        multiple += l

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
