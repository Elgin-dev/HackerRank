#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    mini=0
    maxi=0
    n=len(arr)-1
    for i in range(n):
        mini+=arr[i]
        j=-i-1
        maxi+=arr[j]
    print(mini,maxi)    
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
