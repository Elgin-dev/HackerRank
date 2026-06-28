#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    digit=0
    lower=0
    upper=0
    special=0
    tot_len=0
    overall=0
    for i in range(n):
        if password[i].isalpha():
            if password[i].isupper():
                upper+=1
                tot_len+=1
            else:
                lower+=1
                tot_len+=1
        elif password[i].isdigit():
            digit+=1 
            tot_len+=1
        elif not password[i].isalnum():
            special+=1
            tot_len+=1  
    
    if digit==0:
            overall+=1
    if lower==0:
            overall+=1
    if upper==0:
            overall+=1
    if special==0:
            overall+=1
    need=max(0,6-n)
    return max(overall,need)
                                               
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
