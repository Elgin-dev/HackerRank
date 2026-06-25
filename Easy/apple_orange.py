#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'countApplesAndOranges' function below.
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
def countApplesAndOranges(s, t, a, b, apples, oranges):
    res_a=[]
    res_b=[]
    fall_apple=0
    fall_orange=0
    for i in range(len(apples)):
        ol=a+apples[i]
        res_a.append(ol)  
    for i in range(len(oranges)):
        ol=b+oranges[i]
        res_b.append(ol)
    for i in range(len(res_a)):
        if res_a[i] >= s and res_a[i]<=t:
            fall_apple+=1
    for i in range(len(res_b)):
        if res_b[i] >= s and res_b[i]<=t:
            fall_orange+=1        
    print(fall_apple)
    print(fall_orange)       
                   

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
