#!/bin/python3

import math
import os
import random
import re
import sys
from copy import *

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    sortedarr=deepcopy(arr)
    sortedarr.sort()
    if sortedarr==arr:
        print("yes")
        return
    l=r=-1
    n=len(arr)
    for i in range(n-1):
         if arr[i]>arr[i+1]:
            l=i
            break
    for i in range(n-1,0,-1):
        if arr[i]<arr[i-1] :
            r=i
            break      
    
    temp=deepcopy(arr)
    temp[l],temp[r]=temp[r],temp[l]
    if temp==sortedarr:
        print("yes")
        print("swap",l+1,r+1)
        return
    temp=deepcopy(arr)
    temp=temp[:l]+temp[l:r+1][::-1]+temp[r+1:]
    if temp==sortedarr:    
        print("yes")
        print("reverse",l+1,r+1)
        return 
    print("no")        
             

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
